"""Strategies for generating torch devices."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Final

import torch
from hypothesis import strategies as st

AVAILABLE_CPU_DEVICES: Final = [torch.device("cpu")]
AVAILABLE_CUDA_DEVICES: Final = [torch.device("cuda", i) for i in range(torch.cuda.device_count())]
AVAILABLE_MPS_DEVICES: Final = [torch.device("mps:0")] if torch.backends.mps.is_available() else []
AVAILABLE_META_DEVICES: Final = [torch.device("meta")]

AVAILABLE_PHYSICAL_DEVICES: Final = AVAILABLE_CPU_DEVICES + AVAILABLE_CUDA_DEVICES + AVAILABLE_MPS_DEVICES


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
    if devices is None:
        devices = AVAILABLE_PHYSICAL_DEVICES
    if allow_meta_device:
        devices = list(devices) + AVAILABLE_META_DEVICES
    assert devices is not None
    return st.sampled_from(devices)


st.register_type_strategy(torch.device, device_strategy())
