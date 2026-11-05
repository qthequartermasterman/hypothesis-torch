"""Tests for registering the random torch state."""

import contextlib
import multiprocessing as mp
import sys
import time
import unittest
from collections.abc import Callable, Iterator
from types import FrameType
from typing import Any

import hypothesis
import hypothesis.internal.entropy
import torch
from hypothesis import strategies as st

import hypothesis_torch
from hypothesis_torch.register_random_torch_state import TorchRandomState


class TestRegisterRandomTorchState(unittest.TestCase):
    """Tests for registering the random torch state."""

    def test_register_random_torch_state(self) -> None:
        """Test that the torch random state is registered."""
        self.assertIn(hypothesis_torch.TORCH_RANDOM_WRAPPER, hypothesis.internal.entropy.RANDOMS_TO_MANAGE.values())

    def test_seed_is_deterministic(self) -> None:
        """Test that seeding the wrapper makes the CPU generator deterministic."""
        hypothesis_torch.TORCH_RANDOM_WRAPPER.seed(1234)
        first = torch.rand(8)
        hypothesis_torch.TORCH_RANDOM_WRAPPER.seed(1234)
        second = torch.rand(8)
        torch.testing.assert_close(first, second)

    def test_getstate_setstate_round_trip(self) -> None:
        """Test that restoring a saved state reproduces the same CPU random numbers."""
        state = hypothesis_torch.TORCH_RANDOM_WRAPPER.getstate()
        self.assertIsInstance(state, TorchRandomState)
        first = torch.rand(8)
        hypothesis_torch.TORCH_RANDOM_WRAPPER.setstate(state)
        second = torch.rand(8)
        torch.testing.assert_close(first, second)

    def test_setstate_accepts_bare_cpu_state(self) -> None:
        """Test that setstate accepts a bare CPU generator state, as returned by older versions of getstate."""
        state = torch.random.get_rng_state()
        first = torch.rand(8)
        hypothesis_torch.TORCH_RANDOM_WRAPPER.setstate(state)
        second = torch.rand(8)
        torch.testing.assert_close(first, second)

    def test_cpu_state_restored_after_given(self) -> None:
        """Test that the CPU generator is restored after a Hypothesis test that consumes randomness."""
        before = torch.random.get_rng_state()

        @hypothesis.given(st.integers())
        @hypothesis.settings(max_examples=5, database=None)
        def consumes_randomness(_: int) -> None:
            torch.rand(4)

        consumes_randomness()
        torch.testing.assert_close(before, torch.random.get_rng_state())

    @unittest.skipUnless(torch.cuda.is_available(), "CUDA is not available")
    def test_cuda_state_seeded_and_restored_after_given(self) -> None:
        """Test that an initialized CUDA generator is both seeded per example and restored after a Hypothesis test."""
        torch.cuda.init()
        before = torch.cuda.get_rng_state_all()
        draws: list[torch.Tensor] = []

        @hypothesis.given(st.integers())
        @hypothesis.settings(max_examples=3, database=None)
        def consumes_cuda_randomness(_: int) -> None:
            draws.append(torch.rand(4, device="cuda").cpu())

        consumes_cuda_randomness()
        after = torch.cuda.get_rng_state_all()
        self.assertEqual(len(before), len(after))
        for state_before, state_after in zip(before, after):
            torch.testing.assert_close(state_before, state_after)

        # Hypothesis seeds every example identically, so the CUDA draws should match.
        self.assertGreaterEqual(len(draws), 1)
        for draw in draws[1:]:
            torch.testing.assert_close(draws[0], draw)

    def test_seed_is_fast_and_independent_of_stack_depth(self) -> None:
        """Regression test for slow per-example seeding (issue #266).

        Hypothesis seeds torch before every example, so the cost of `TorchRandomWrapper.seed` is paid once per example
        of every `@given` test. It used to call `torch.manual_seed`, which, for every lazily-initialized accelerator
        backend (CUDA, XPU, MTIA) that is not yet initialized, queues a deferred seed and captures
        `traceback.format_stack()` to report where the call came from. Formatting the stack costs time proportional to
        its depth, and stacks under pytest and Hypothesis are deep: it measured ~3.4 ms per example in a real test
        suite, more than half the runtime of cheap `@given` tests, versus ~1 us to seed the CPU generator directly.

        This test times `seed` directly, called from a shallow and from a deep stack, and checks that:

        - it stays well under a generous absolute budget at depth, which the old implementation exceeded several times
          over even without the extra pytest/Hypothesis frames; and
        - it does not get meaningfully slower with stack depth, which is the signature of capturing stack traces.

        Timings use the best of several repeats to reduce noise, and the thresholds leave a wide margin so that slow or
        busy CI machines do not cause flaky failures. `test_given_seeding_does_not_queue_deferred_seeds` checks the
        underlying cause deterministically.
        """
        calls_per_repeat = 200
        repeats = 5
        deep_stack_depth = 200
        # Measured on one machine at depth 200: the fixed wrapper takes ~2-10 us per call; the old one took ~0.9-1.3 ms.
        absolute_budget_s = 250e-6
        max_deep_to_shallow_ratio = 3.0
        noise_allowance_s = 20e-6

        def best_seconds_per_call() -> float:
            best = float("inf")
            for _ in range(repeats):
                start = time.perf_counter()
                for i in range(calls_per_repeat):
                    hypothesis_torch.TORCH_RANDOM_WRAPPER.seed(i)
                best = min(best, (time.perf_counter() - start) / calls_per_repeat)
            return best

        def at_depth(depth: int) -> float:
            return at_depth(depth - 1) if depth else best_seconds_per_call()

        state = hypothesis_torch.TORCH_RANDOM_WRAPPER.getstate()
        try:
            shallow = at_depth(0)
            deep = at_depth(deep_stack_depth)
        finally:
            hypothesis_torch.TORCH_RANDOM_WRAPPER.setstate(state)

        self.assertLess(
            deep,
            absolute_budget_s,
            f"seed took {deep * 1e6:.1f} us per call at stack depth {deep_stack_depth}",
        )
        self.assertLess(
            deep,
            shallow * max_deep_to_shallow_ratio + noise_allowance_s,
            f"seed took {shallow * 1e6:.1f} us per call at stack depth 0 but {deep * 1e6:.1f} us at depth "
            f"{deep_stack_depth}; seeding should not depend on stack depth",
        )

    def test_uninitialized_backends_are_not_touched(self) -> None:
        """Test that the wrapper neither initializes accelerator backends nor queues deferred seeds for them.

        Runs in a fresh process so that CUDA is guaranteed to be uninitialized.
        """
        _run_in_fresh_process(_check_uninitialized_backends_are_not_touched)

    def test_given_seeding_does_not_queue_deferred_seeds(self) -> None:
        """Test that a real `@given` test seeds torch through the wrapper without torch capturing any stack traces.

        Guards the per-example cost end to end: if seeding stopped going through `TorchRandomWrapper`, or anything in
        Hypothesis's seeding path called `torch.manual_seed` again, torch would capture a stack trace per example.
        Runs in a fresh process so that CUDA is guaranteed to be uninitialized.
        """
        _run_in_fresh_process(_check_given_seeding_does_not_queue_deferred_seeds)


def _run_in_fresh_process(target: Callable[[], None]) -> None:
    """Run `target` in a freshly spawned interpreter and assert that it succeeded."""
    ctx = mp.get_context("spawn")
    p = ctx.Process(target=target)
    p.start()
    p.join()
    assert p.exitcode == 0, f"{target.__name__} failed in a subprocess with exit code {p.exitcode}"


@contextlib.contextmanager
def _record_torch_stack_captures() -> Iterator[list[str]]:
    """Record calls to `traceback.format_stack` made directly by torch modules.

    torch queues a deferred call for an uninitialized lazy backend (CUDA, XPU, MTIA) by capturing
    `traceback.format_stack()`, whose cost grows with stack depth. That is what made per-example seeding slow.

    Yields:
        A list that is appended with the calling module's name for every capture made by torch.
    """
    import traceback
    from unittest import mock

    captures: list[str] = []
    real_format_stack = traceback.format_stack

    def spy(f: FrameType | None = None, limit: int | None = None) -> list[str]:
        caller = sys._getframe(1).f_globals.get("__name__", "")
        if caller.split(".")[0] == "torch":
            captures.append(caller)
        return real_format_stack(f, limit)

    with mock.patch.object(traceback, "format_stack", spy):
        yield captures


def _lazy_backends() -> list[Any]:
    """Return the lazily-initialized accelerator backend modules available in this torch build."""
    return [getattr(torch, name) for name in ("cuda", "xpu", "mtia") if hasattr(torch, name)]


def _check_uninitialized_backends_are_not_touched() -> None:
    """Seed, save and restore via the wrapper, and check that no lazy backend was initialized or had a seed queued."""
    assert not any(backend.is_initialized() for backend in _lazy_backends())

    with _record_torch_stack_captures() as captures:
        state = hypothesis_torch.TORCH_RANDOM_WRAPPER.getstate()
        hypothesis_torch.TORCH_RANDOM_WRAPPER.seed(1234)
        hypothesis_torch.TORCH_RANDOM_WRAPPER.setstate(state)

    assert not captures, captures
    assert not any(backend.is_initialized() for backend in _lazy_backends())


def _check_given_seeding_does_not_queue_deferred_seeds() -> None:
    """Run a `@given` test and check that it seeds torch via the wrapper without torch capturing stack traces."""
    from unittest import mock

    assert not any(backend.is_initialized() for backend in _lazy_backends())
    wrapper = hypothesis_torch.TORCH_RANDOM_WRAPPER
    examples = 0

    @hypothesis.given(st.integers())
    @hypothesis.settings(max_examples=10, database=None)
    def uses_torch_randomness(_: int) -> None:
        nonlocal examples
        examples += 1
        torch.rand(4)

    with mock.patch.object(wrapper, "seed", wraps=wrapper.seed) as seed, _record_torch_stack_captures() as captures:
        uses_torch_randomness()

    assert examples > 0
    # Hypothesis must seed torch through the registered wrapper, once per example (plus any internal runs).
    assert seed.call_count >= examples, (seed.call_count, examples)
    assert not captures, captures
    assert not any(backend.is_initialized() for backend in _lazy_backends())
