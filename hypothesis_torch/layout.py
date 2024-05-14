"""Hypothesis strategies for generating torch layouts."""

from __future__ import annotations

from collections.abc import Sequence

import torch
from hypothesis import strategies as st

SUPPORTED_LAYOUTS: list[torch.layout] = [
    torch.strided,
    torch.sparse_coo,
]


def layout_strategy(accepted_layouts: Sequence[torch.layout] | None = None) -> st.SearchStrategy[torch.layout]:
    """Strategy for generating torch layouts.

    Args:
        accepted_layouts: A sequence of layouts to sample from. If None, all supported layouts are sampled.
    """
    if accepted_layouts is None:
        accepted_layouts = SUPPORTED_LAYOUTS
    return st.sampled_from(accepted_layouts)


st.register_type_strategy(torch.layout, layout_strategy())
