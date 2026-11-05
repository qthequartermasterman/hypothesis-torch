"""Register a random.Random-compatible shim for `torch.random` with Hypothesis."""

from __future__ import annotations

from typing import Any, NamedTuple

import hypothesis
import hypothesis.internal.entropy
import torch

# Accelerator backends that torch initializes lazily. `torch.manual_seed` seeds these even when they are not yet
# initialized, by queueing a deferred call that captures a formatted stack trace every time (slow under deep stacks).
_LAZY_BACKENDS = ("cuda", "xpu", "mtia")


class TorchRandomState(NamedTuple):
    """Snapshot of the torch RNG state managed by `TorchRandomWrapper`.

    Attributes:
        cpu: The state of the default CPU generator.
        devices: The generator states of each accelerator backend that was active when the snapshot was taken, keyed by
            backend name (e.g. `"cuda"`).
    """

    cpu: torch.Tensor
    devices: dict[str, Any]


def _active_lazy_backends() -> list[str]:
    """Return the names of the lazily-initialized accelerator backends that are already initialized."""
    active = []
    for name in _LAZY_BACKENDS:
        is_initialized = getattr(getattr(torch, name, None), "is_initialized", None)
        if is_initialized is not None and is_initialized():
            active.append(name)
    return active


def _mps_is_active() -> bool:
    """Return whether the MPS backend is available. MPS is not lazily initialized, so managing it is cheap."""
    mps_backend = getattr(torch.backends, "mps", None)
    return mps_backend is not None and mps_backend.is_available()


class TorchRandomWrapper:
    """Shim for `torch.random` to match the random.Random interface.

    Hypothesis's random state manager requires a random.Random-compatible object. Before each example, Hypothesis
    calls `getstate` and then `seed`, and after the example it calls `setstate` with the saved state.

    The wrapper always seeds, saves and restores the default CPU generator. It also seeds, saves and restores the
    generators of every accelerator backend that is active at the start of the example: MPS when available, and CUDA,
    XPU and MTIA only once they have been initialized. Seeding therefore never initializes a device, and every generator
    that is seeded is also restored afterwards. As a consequence, if a test initializes e.g. CUDA for the first time
    inside an example, that example's CUDA generator is not seeded by Hypothesis (later examples are).

    Custom (`privateuse1`) device backends are not managed.
    """

    def seed(self, seed: int) -> None:
        """Seed the CPU generator and the generators of every active accelerator backend.

        Args:
            seed: The seed to use.
        """
        seed = int(seed)
        for name in _active_lazy_backends():
            getattr(torch, name).manual_seed_all(seed)
        if _mps_is_active():
            torch.mps.manual_seed(seed)
        torch.default_generator.manual_seed(seed)

    def getstate(self) -> TorchRandomState:
        """Return the state of the CPU generator and of the generators of every active accelerator backend.

        Returns:
            A snapshot that can be passed to `setstate`.
        """
        devices: dict[str, Any] = {name: getattr(torch, name).get_rng_state_all() for name in _active_lazy_backends()}
        if _mps_is_active():
            devices["mps"] = torch.mps.get_rng_state()
        return TorchRandomState(cpu=torch.default_generator.get_state(), devices=devices)

    def setstate(self, state: TorchRandomState | torch.Tensor) -> None:
        """Restore a state previously returned by `getstate`.

        Args:
            state: The state to restore. A bare tensor is treated as the state of the CPU generator alone.
        """
        if isinstance(state, torch.Tensor):
            torch.default_generator.set_state(state)
            return
        for name, device_state in state.devices.items():
            if name == "mps":
                torch.mps.set_rng_state(device_state)
            else:
                getattr(torch, name).set_rng_state_all(device_state)
        torch.default_generator.set_state(state.cpu)


TORCH_RANDOM_WRAPPER = TorchRandomWrapper()


def _register_random_torch_state() -> None:
    """Register the random torch state with Hypothesis."""
    # Pyright is unhappy with the typing of WeakValueDictionary.values()
    # error: Operator "not in" not supported for types "TorchRandomWrapper" and "Iterator[RandomLike]"
    # (reportOperatorIssue)
    if TORCH_RANDOM_WRAPPER not in hypothesis.internal.entropy.RANDOMS_TO_MANAGE.values():  # type: ignore
        hypothesis.register_random(TORCH_RANDOM_WRAPPER)
