"""Strategies for generating PyTorch tensors."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import hypothesis.extra.numpy as numpy_st
import torch
from hypothesis import strategies as st
import hypothesis

from hypothesis_torch import dtype as dtype_module


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

    Returns:
        A strategy for generating PyTorch tensors.

    """
    # We will pre-sample the dtype so that we can cast it to a concrete numpy dtype
    if isinstance(dtype, st.SearchStrategy):
        dtype = draw(dtype)
    numpy_dtype = dtype_module.numpy_dtype_map[dtype]

    # We will pre-sample the device so that we can cast it to a concrete torch device
    if isinstance(device, st.SearchStrategy):
        device = draw(device)

    # INCOMPATIBILITY HANDLING
    # MPS devices do not support tensors with dtype torch.float64 and bfloat16
    hypothesis.assume(not (device is not None and device.type == "mps" and dtype in (torch.float64, torch.bfloat16)))
    # If the dtype is an integer, we need to make sure that the elements are integers within the dtype's range
    if dtype in dtype_module.INT_DTYPES and isinstance(elements, st.SearchStrategy):
        info = torch.iinfo(dtype)
        elements = elements.filter(lambda x: info.min <= x <= info.max)

    if isinstance(unique, st.SearchStrategy):
        unique = draw(unique)

    ndarray_strategy = numpy_st.arrays(numpy_dtype, shape, elements=elements, fill=fill, unique=unique)
    tensor = draw(ndarray_strategy.map(torch.from_numpy))

    return tensor.to(dtype=dtype, device=device)  # Final casting to the desired dtype and device


st.register_type_strategy(
    torch.Tensor,
    tensor_strategy(
        dtype=dtype_module.dtype_strategy(),
        shape=st.integers(min_value=0, max_value=10),  # Discourage large tensors
    ),
)
