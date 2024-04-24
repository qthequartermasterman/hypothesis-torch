"""Strategies for generating PyTorch dtypes."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Mapping

from typing_extensions import Final

import numpy as np
import numpy.typing as npt
import torch
from hypothesis import strategies as st

SIGNED_INT_DTYPES: Final[tuple[torch.dtype, ...]] = (
    torch.int8,
    torch.int16,
    torch.int32,
    torch.int64,
)
"""All signed integer dtypes supported by PyTorch."""
UNSIGNED_INT_DTYPES: Final[tuple[torch.dtype, ...]] = (torch.uint8,)
"""All unsigned integer dtypes supported by PyTorch."""
INT_DTYPES: Final[tuple[torch.dtype, ...]] = SIGNED_INT_DTYPES + UNSIGNED_INT_DTYPES
"""All integer (both signed and unsigned) dtypes supported by PyTorch."""

FLOAT_DTYPES: Final[tuple[torch.dtype, ...]] = (
    torch.float16,
    torch.float32,
    torch.float64,
)
"""All floating point dtypes supported by PyTorch."""
BFLOAT_DTYPES: Final[tuple[torch.dtype, ...]] = (torch.bfloat16,)
"""All brain-float dtypes supported by PyTorch."""
COMPLEX_DTYPES: Final[tuple[torch.dtype, ...]] = (
    torch.complex64,
    torch.complex128,
)
"""All complex dtypes supported by PyTorch."""
BOOL_DTYPES: Final[tuple[torch.dtype, ...]] = (torch.bool,)
"""All boolean dtypes supported by PyTorch."""

ALL_DTYPES: Final[tuple[torch.dtype, ...]] = INT_DTYPES + FLOAT_DTYPES + BFLOAT_DTYPES + COMPLEX_DTYPES + BOOL_DTYPES
"""All dtypes supported by PyTorch."""

numpy_dtype_map: Final[Mapping[torch.dtype, npt.DTypeLike]] = {
    torch.int8: np.int8,
    torch.int16: np.int16,
    torch.int32: np.int32,
    torch.int64: np.int64,
    torch.uint8: np.uint8,
    torch.float16: float,
    torch.float32: float,
    torch.float64: float,
    torch.bfloat16: float,
    torch.complex64: complex,
    torch.complex128: complex,
    torch.bool: np.bool_,
}
"""A mapping from torch dtypes to numpy dtypes. Useful for generating tensors of arbitrary dtypes from the builtin
numpy strategies."""

assert set(numpy_dtype_map.keys()) == set(ALL_DTYPES)


def dtype_strategy(dtypes: Sequence[torch.dtype] | None = None) -> st.SearchStrategy[torch.dtype]:
    """Strategy for generating torch dtypes.

    Args:
        dtypes: A strategy for generating elements of the dtype. If `None`, all dtypes are sampled.

    Returns:
        A strategy for generating torch dtypes.
    """
    if dtypes is None:
        dtypes = ALL_DTYPES
    return st.sampled_from(dtypes)


st.register_type_strategy(torch.dtype, dtype_strategy())
