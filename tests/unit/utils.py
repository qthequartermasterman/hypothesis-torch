"""Meta-strategies for hypothesis tests."""

from __future__ import annotations

from typing import Any, Callable

from hypothesis import strategies as st
from typing_extensions import ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")


@st.composite
def meta_strategy_constraints(
    draw: st.DrawFn,
    strategy_func: Callable[P, st.SearchStrategy[T]],
    **kwargs: dict[str, Any | st.SearchStrategy[Any]],
) -> tuple[T, dict[str, Any]]:
    """A strategy that takes another strategy, and allows specifying constraints on that strategy."""
    for key, value in kwargs.items():
        if isinstance(value, st.SearchStrategy):
            kwargs[key] = draw(value)
    strategy = strategy_func(**kwargs)
    return draw(strategy), kwargs
