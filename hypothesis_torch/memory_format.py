"""Hypothesis strategies for generating torch memory formats."""

from __future__ import annotations

from collections.abc import Sequence

import torch
from hypothesis import strategies as st

SUPPORTED_MEMORY_FORMATS: list[torch.memory_format] = [
    torch.contiguous_format,
    torch.channels_last,
    torch.channels_last_3d,
]


def memory_format_strategy(
    accepted_formats: Sequence[torch.memory_format] | None = None,
) -> st.SearchStrategy[torch.memory_format]:
    """Strategy for generating torch layouts.

    Args:
        accepted_formats: A sequence of layouts to sample from. If None, all supported layouts are sampled.
    """
    if accepted_formats is None:
        accepted_formats = SUPPORTED_MEMORY_FORMATS
    return st.sampled_from(accepted_formats)


st.register_type_strategy(torch.memory_format, memory_format_strategy())
