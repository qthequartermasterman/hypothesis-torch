"""Strategies for generating PyTorch tensors."""

from __future__ import annotations

import struct
from collections.abc import Mapping
from typing import Any, Sequence, Literal

from hypothesis.internal.floats import float_of
from typing_extensions import Final

import hypothesis.extra.numpy as numpy_st
import torch
from hypothesis import strategies as st, reject
import hypothesis

import hypothesis_torch
from hypothesis_torch import dtype as dtype_module

_NOT_MPS_DEVICES: Final[Sequence[torch.device]] = (
    hypothesis_torch.AVAILABLE_CPU_DEVICES + hypothesis_torch.AVAILABLE_CUDA_DEVICES
)
"""All devices that are not MPS devices (since MPS devices do not yet have full torch support)."""

_ALLOWED_DEVICES_FROM_DTYPE: Final[Mapping[torch.dtype, Sequence[torch.device]]] = {
    torch.bool: hypothesis_torch.AVAILABLE_PHYSICAL_DEVICES,
    torch.uint8: hypothesis_torch.AVAILABLE_PHYSICAL_DEVICES,
    torch.int8: hypothesis_torch.AVAILABLE_PHYSICAL_DEVICES,
    torch.int16: hypothesis_torch.AVAILABLE_PHYSICAL_DEVICES,
    torch.int32: hypothesis_torch.AVAILABLE_PHYSICAL_DEVICES,
    torch.int64: hypothesis_torch.AVAILABLE_PHYSICAL_DEVICES,
    torch.float16: hypothesis_torch.AVAILABLE_PHYSICAL_DEVICES,
    torch.float32: hypothesis_torch.AVAILABLE_PHYSICAL_DEVICES,
    # MPS devices do not support tensors with dtype torch.float64 and bfloat16
    torch.float64: _NOT_MPS_DEVICES,
    torch.bfloat16: _NOT_MPS_DEVICES,
    torch.complex64: hypothesis_torch.AVAILABLE_PHYSICAL_DEVICES,
    torch.complex128: hypothesis_torch.AVAILABLE_PHYSICAL_DEVICES,
}
"""A mapping from dtype to the devices that support that dtype."""


def _reinterpret_bits(
    x: float, from_: Literal["!f", "!e"], to: Literal["!f", "!e"], truncate_bytes: int | None = None
) -> float:
    """Reinterpret the bits of a float.

    This function is used to ensure that only floats that can be represented exactly by a certain dtype are generated.

    Adapted from `hypothesis.internal.floats.reinterpret_bits`.

    Args:
        x: The float to reinterpret.
        from_: The format of the input float.
        to: The format of the output float.
        truncate_bytes: The number of bytes to truncate from the end of the float.

    Returns:
        The re-interpreted float.
    """
    if truncate_bytes is None:
        return struct.unpack(to, struct.pack(from_, x))[0]
    return struct.unpack(to, struct.pack(from_, x)[:-truncate_bytes] + b"\x00" * truncate_bytes)[0]


def downcast(x: float, dtype: torch.dtype) -> float:
    """Downcast a float to a smaller width.

    This function is used to ensure that only floats that can be represented exactly are generated.

    Adapted from `hypothesis.strategies.numbers.floats`.

    Args:
        x: The float to downcast.
        dtype: The dtype to downcast to.

    Returns:
        The downcasted float.
    """
    try:
        assert dtype in (torch.float64, torch.float32, torch.float16, torch.bfloat16)
        if dtype == torch.float64:
            return x
        elif dtype == torch.float32:
            return _reinterpret_bits(x, "!f", "!f")
        elif dtype == torch.bfloat16:
            return _reinterpret_bits(x, "!f", "!f", truncate_bytes=2)
        elif dtype == torch.float16:
            return _reinterpret_bits(x, "!e", "!e")
        else:
            raise ValueError(f"Unsupported dtype: {dtype}")
    except OverflowError:
        hypothesis.reject()


@st.composite
def tensor_strategy(
    draw: st.DrawFn,
    dtype: torch.dtype | st.SearchStrategy[torch.dtype],
    shape: int | st.SearchStrategy[int] | tuple[int, ...] | st.SearchStrategy[tuple[int, ...]],
    *,
    elements: st.SearchStrategy[Any] | Mapping[str, Any] | None = None,
    fill: st.SearchStrategy[Any] | None = None,
    unique: bool | st.SearchStrategy[bool] = False,
    device: torch.device | st.SearchStrategy[torch.device] | None = None,
    requires_grad: bool | st.SearchStrategy[bool] | None = None,
    pin_memory: bool | st.SearchStrategy[bool] | None = None,
    layout: torch.layout | st.SearchStrategy[torch.layout] | None = None,
    memory_format: torch.memory_format | st.SearchStrategy[torch.memory_format] | None = None,
) -> torch.Tensor:
    """A strategy for generating PyTorch tensors.

    Args:
        draw: The draw function provided by `hypothesis`.
        dtype: Any PyTorch dtype or a strategy for generating PyTorch dtypes.
        shape: The shape of the tensor. Can be an integer >= 0, a tuple of such integers, or a strategy for generating
            such values.
        elements: A strategy for generating elements of the tensor. If `None`, a suitable strategy is inferred from
            the dtype. Note that this may give any legal value (including NaNs and infinities for floats).
        fill: A strategy for generating a single background value for the tensor. If None, a suitable default will
            be inferred based on the other arguments. If set to `~hypothesis.strategies.nothing` then filling
            behaviour will be disabled entirely and every element will be generated independently.
        unique: Whether the tensor's elements should all be distinct from one another. Note that multiple NaN values
            may still be allowed.
        device: The device on which to place the tensor. If None, the default device is used.
        requires_grad: Whether the tensor requires gradients. If None, a suitable default will be inferred based on
            the other arguments.
        pin_memory: Whether the tensor should be pinned in memory. If None, a suitable default will be inferred based
            on the other arguments.
        layout: The memory layout of the tensor. If None, a suitable default will be inferred based on the other
            arguments. Note that sparse layouts are not supported on MPS devices.
        memory_format: The memory format of the tensor. If None, a suitable default will be inferred based on the other
            arguments. Note that channel_last memory formats are only supported for 4D tensors and channel_last_3d
            memory formats are only supported for 5D tensors.

    Returns:
        A strategy for generating PyTorch tensors.

    """
    # We will pre-sample the dtype so that we can cast it to a concrete numpy dtype
    if isinstance(dtype, st.SearchStrategy):
        dtype = draw(dtype)
    numpy_dtype = dtype_module.numpy_dtype_map[dtype]

    # We will pre-sample the device so that we can cast it to a concrete torch device
    if device is None:
        device = st.sampled_from(_ALLOWED_DEVICES_FROM_DTYPE[dtype])
    if isinstance(device, st.SearchStrategy):
        device = draw(device)
    # MPS devices do not support tensors with dtype torch.float64 and bfloat16
    hypothesis.assume(device is None or device.type != "mps" or dtype not in (torch.float64, torch.bfloat16))

    if layout is None:
        layout = st.from_type(torch.layout)
    if isinstance(layout, st.SearchStrategy):
        layout = draw(layout)
    # MPS devices do not support sparse tensors
    hypothesis.assume(device is None or device.type != "mps" or layout != torch.sparse_coo)

    # If the dtype is an integer, we need to make sure that the elements are integers within the dtype's range
    if dtype in dtype_module.INT_DTYPES and isinstance(elements, st.SearchStrategy):
        info = torch.iinfo(dtype)
        elements = elements.filter(lambda x: info.min <= x <= info.max)

    # If the dtype is a float, then we need to make sure that only elements that can be represented exactly are
    # generated
    if dtype in {torch.bfloat16, torch.float32, torch.float16} and elements is not None:
        elements = elements.map(lambda x: downcast(x, dtype))

    if isinstance(unique, st.SearchStrategy):
        unique = draw(unique)

    ndarray_strategy = numpy_st.arrays(numpy_dtype, shape, elements=elements, fill=fill, unique=unique)
    tensor = draw(ndarray_strategy.map(torch.from_numpy))

    if pin_memory is None:
        pin_memory = st.booleans() if device.type == "cuda" else False
    if isinstance(pin_memory, st.SearchStrategy):
        pin_memory = draw(pin_memory)
    if pin_memory and device.type == "cuda":
        tensor = tensor.pin_memory()

    tensor = tensor.to(device=device, dtype=dtype)

    if requires_grad is None:
        requires_grad = st.booleans() if dtype in dtype_module.FLOAT_DTYPES else False
    if isinstance(requires_grad, st.SearchStrategy):
        requires_grad = draw(requires_grad)
    tensor.requires_grad_(requires_grad)

    if layout == torch.strided:
        tensor = tensor.contiguous()
    elif layout == torch.sparse_coo:
        # TODO: Implement coalesced handling
        tensor = tensor.to_sparse_coo()
    else:
        raise ValueError(f"Unsupported layout: {layout}")

    # MEMORY FORMAT HANDLING
    if memory_format is None:
        permitted_memory_formats = [torch.contiguous_format]
        if len(tensor.shape) == 4:
            permitted_memory_formats.append(torch.channels_last)
        if len(tensor.shape) == 5:
            permitted_memory_formats.append(torch.channels_last_3d)
        memory_format = st.sampled_from(permitted_memory_formats)
    if isinstance(memory_format, st.SearchStrategy):
        memory_format = draw(memory_format)
    # Filter out memory formats that are not supported by the tensor's shape, in case a user-specified strategy is used.
    # channel_last memory format is only supported for 4D tensors
    hypothesis.assume(memory_format != torch.channels_last or len(tensor.shape) == 4)
    # channel_last_3d memory format is only supported for 5D tensors
    hypothesis.assume(memory_format != torch.channels_last_3d or len(tensor.shape) == 5)
    tensor = tensor.to(memory_format=memory_format)

    return tensor


st.register_type_strategy(
    torch.Tensor,
    tensor_strategy(
        dtype=dtype_module.dtype_strategy(),
        shape=st.integers(min_value=0, max_value=10),  # Discourage large tensors
    ),
)
