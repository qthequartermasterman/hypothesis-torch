"""Tests for registering the random torch state."""

import multiprocessing as mp
import unittest

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

    def test_uninitialized_backends_are_not_touched(self) -> None:
        """Test that the wrapper neither initializes accelerator backends nor queues deferred seeds for them.

        Runs in a fresh process so that CUDA is guaranteed to be uninitialized.
        """
        ctx = mp.get_context("spawn")
        p = ctx.Process(target=_check_uninitialized_backends_are_not_touched)
        p.start()
        p.join()
        self.assertEqual(p.exitcode, 0)


def _check_uninitialized_backends_are_not_touched() -> None:
    """Seed, save and restore via the wrapper, and check that no lazy backend was initialized or had a seed queued.

    torch queues a deferred call for an uninitialized lazy backend by capturing `traceback.format_stack()`, which is
    what made per-example seeding slow under deep stacks.
    """
    import traceback
    from unittest import mock

    import torch

    import hypothesis_torch

    lazy_backends = [getattr(torch, name) for name in ("cuda", "xpu", "mtia") if hasattr(torch, name)]
    assert not any(backend.is_initialized() for backend in lazy_backends)

    with mock.patch.object(traceback, "format_stack", wraps=traceback.format_stack) as format_stack:
        state = hypothesis_torch.TORCH_RANDOM_WRAPPER.getstate()
        hypothesis_torch.TORCH_RANDOM_WRAPPER.seed(1234)
        hypothesis_torch.TORCH_RANDOM_WRAPPER.setstate(state)

    assert format_stack.call_count == 0, format_stack.call_count
    assert not any(backend.is_initialized() for backend in lazy_backends)
