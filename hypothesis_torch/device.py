"""Strategies for generating torch devices."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Callable

import torch
from hypothesis import strategies as st
from typing_extensions import TypeAlias

LAZY_LIST_OF_DEVICES: TypeAlias = Callable[[], list[torch.device]]


def mps_devices() -> list[torch.device]:
    """Lazily create a list of all available MPS devices."""
    if torch.backends.mps.is_available():
        return [torch.device("mps:0")]
    return []


def cuda_devices() -> list[torch.device]:
    """Lazily create a list of all available CUDA devices."""
    if torch.cuda.is_available():
        return [torch.device("cuda", i) for i in range(torch.cuda.device_count())]
    return []


def physical_devices() -> list[torch.device]:
    """Lazily create a list of all available physical devices."""
    out = [torch.device("cpu")]
    out.extend(mps_devices())
    out.extend(cuda_devices())
    return out


def not_mps_devices() -> list[torch.device]:
    """Lazily create a list of non-MPS devices."""
    return [d for d in physical_devices() if d.type != "mps"]


def sampled_devices(get_list: LAZY_LIST_OF_DEVICES) -> st.SearchStrategy[torch.device]:
    """Lazily sample from devices.

    The list of devices is not generated until sampling time, to avoid eagerly initializing cuda.

    Args:
        get_list: Lazy list of devices.
    """
    return st.deferred(lambda: st.sampled_from(get_list()))


def device_strategy(
    *,
    devices: Sequence[torch.device] | None = None,
    allow_meta_device: bool = False,
) -> st.SearchStrategy[torch.device]:
    """Strategy for generating torch devices.

    Args:
        devices: A sequence of devices to sample from. If None, all available devices are sampled.
        allow_meta_device: Whether to allow the meta device.

    Returns:
        A strategy for generating torch devices.

    """
    # wrap the provided devices in a no-arg function
    base_fn: LAZY_LIST_OF_DEVICES = physical_devices if devices is None else lambda: list(devices)

    if allow_meta_device:

        def lazy_with_meta(fn: LAZY_LIST_OF_DEVICES) -> LAZY_LIST_OF_DEVICES:
            """Add the meta device to a list of lazily accessed torch devices.

            Args:
                fn: A function that lazily fetches a list of torch devices.

            Returns:
                New lazy list of devices, but with the meta device added.
            """

            def add_meta() -> list[torch.device]:
                """Add the meta device to the lazy list.

                Returns:
                    New lazy list of devices, but with the meta device added.
                """
                return [*fn(), torch.device("meta")]

            return add_meta

        base_fn = lazy_with_meta(base_fn)

    return sampled_devices(base_fn)


st.register_type_strategy(torch.device, device_strategy())
