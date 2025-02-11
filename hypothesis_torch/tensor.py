"""Strategies for generating PyTorch tensors."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any, Final

import hypothesis
import hypothesis.extra.numpy as numpy_st
import hypothesis.internal.floats
import torch
from hypothesis import strategies as st

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


@st.composite
def tensor_strategy(
    draw: st.DrawFn,
    dtype: torch.dtype | st.SearchStrategy[torch.dtype],
    shape: int | st.SearchStrategy[int] | tuple[int, ...] | st.SearchStrategy[tuple[int, ...]],
    *,
    elements: st.SearchStrategy[Any] | None = None,
    fill: st.SearchStrategy[Any] | None = None,
    unique: bool | st.SearchStrategy[bool] = False,
    device: torch.device | st.SearchStrategy[torch.device] | None = None,
    requires_grad: bool | st.SearchStrategy[bool] | None = None,
    pin_memory: bool | st.SearchStrategy[bool] | None = None,
    layout: torch.layout | st.SearchStrategy[torch.layout] | None = None,
    memory_format: torch.memory_format | st.SearchStrategy[torch.memory_format] | None = None,
    names: bool | st.SearchStrategy[bool] = False,
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
        names: Whether to give explicit names to the tensor's dimensions, using the "Named Tensors" API. `names` will
            default to False until the Named Tensors API is no longer experimental.

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
    if dtype in dtype_module.FLOAT_DTYPES and elements is not None:
        if dtype == torch.bfloat16:
            # Since we do not directly support bfloat16 in numpy, we will generate float32.
            # This still means that we will occasionally generate values that exceed the max/min of bfloat16.
            # All other values (within the range) will be simply truncated below when casting the numpy array to
            # a bfloat16 tensor.
            bfloat16_info = torch.finfo(torch.bfloat16)
            elements = elements.filter(lambda x: bfloat16_info.min <= x <= bfloat16_info.max)

        width = dtype_module.float_width_map[dtype]
        if width < 64:

            def downcast(x: float) -> float:
                """Downcast a float to a smaller width.

                This function is used to ensure that only floats that can be represented exactly are generated.

                Adapted from `hypothesis.strategies.numbers.floats`.

                Args:
                    x: The float to downcast.

                Returns:
                    The downcasted float.
                """
                try:
                    return hypothesis.internal.floats.float_of(x, width)
                except OverflowError:  # pragma: no cover
                    hypothesis.reject()

            elements = elements.map(downcast)

    if isinstance(unique, st.SearchStrategy):
        unique = draw(unique)

    ndarray_strategy = numpy_st.arrays(numpy_dtype, shape, elements=elements, fill=fill, unique=unique)
    tensor = draw(ndarray_strategy.map(torch.from_numpy))

    if pin_memory is None:
        pin_memory = st.booleans() if device.type == "cuda" else False
    if isinstance(pin_memory, st.SearchStrategy):
        pin_memory = draw(pin_memory)
    if pin_memory and device.type == "cuda":  # pragma: no cover
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
    else:  # pragma: no cover
        raise ValueError(f"Unsupported layout: {layout}")

    # MEMORY FORMAT HANDLING
    if memory_format is None:
        permitted_memory_formats = get_permitted_memory_formats(tensor)
        memory_format = st.sampled_from(permitted_memory_formats)
    if isinstance(memory_format, st.SearchStrategy):
        memory_format = draw(memory_format)
    # Filter out memory formats that are not supported by the tensor's shape, in case a user-specified strategy is used.
    # channel_last memory format is only supported for 4D tensors
    hypothesis.assume(memory_format != torch.channels_last or len(tensor.shape) == 4)
    # channel_last_3d memory format is only supported for 5D tensors
    hypothesis.assume(memory_format != torch.channels_last_3d or len(tensor.shape) == 5)
    # Pyright/mypy falsely reports an error here on py3.9 torch 2.1.2.
    tensor = tensor.to(memory_format=memory_format)  # type: ignore

    if isinstance(names, st.SearchStrategy):
        names = draw(names)
    if names:
        # Named tensors only supported on CPU/CUDA.
        hypothesis.assume(tensor.device.type in {"cpu", "cuda"})
        # Named tensors only support strided tensors
        hypothesis.assume(layout == torch.strided)
        num_dimensions = tensor.ndim
        individual_dimensions_should_have_name = draw(st.tuples(*[st.booleans() for _ in range(num_dimensions)]))
        # At least one dimension needs to be named, but not all of them have to be.
        hypothesis.assume(any(individual_dimensions_should_have_name))
        individual_dimensions_names = [
            f"dim{i}" if should_name else None for i, should_name in enumerate(individual_dimensions_should_have_name)
        ]
        tensor = tensor.rename(*individual_dimensions_names)

    return tensor


def get_permitted_memory_formats(tensor: torch.Tensor) -> list[torch.memory_format]:
    """Get the memory formats that are permitted for a tensor.

    Args:
        tensor: The tensor.

    Returns:
        A list of memory formats that are permitted for the tensor.
    """
    if tensor.layout != torch.strided:
        return [torch.preserve_format]
    permitted_memory_formats = [torch.contiguous_format]
    if len(tensor.shape) == 4:
        permitted_memory_formats.append(torch.channels_last)
    if len(tensor.shape) == 5:
        permitted_memory_formats.append(torch.channels_last_3d)
    return permitted_memory_formats


st.register_type_strategy(
    torch.Tensor,
    tensor_strategy(
        dtype=dtype_module.dtype_strategy(),
        shape=st.integers(min_value=0, max_value=10),  # Discourage large tensors
    ),
)
