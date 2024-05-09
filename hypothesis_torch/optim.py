"""Strategies for generating torch optimizers."""

from __future__ import annotations

from typing import Sequence, Final, Callable, Iterator
from typing_extensions import TypeAlias

import hypothesis
import torch.optim
import inspect

from hypothesis import strategies as st
from hypothesis_torch import inspection_util

OptimizerConstructorWithOnlyParameters: TypeAlias = Callable[[Iterator[torch.nn.Parameter]], torch.optim.Optimizer]

OPTIMIZERS: Final[tuple[type[torch.optim.Optimizer], ...]] = tuple(
    optimizer
    for optimizer in inspection_util.get_all_subclasses(torch.optim.Optimizer)
    if optimizer is not torch.optim.Optimizer and "NewCls" not in optimizer.__name__
)

_ZERO_TO_ONE_FLOATS: Final[st.SearchStrategy[float]] = st.floats(
    min_value=0.0, max_value=1.0, exclude_max=True, exclude_min=True
)


@st.composite
def betas(draw: st.DrawFn) -> tuple[float, float]:
    """Strategy for generating beta1 and beta2 values for optimizers.

    Args:
        draw: The draw function provided by `hypothesis`.

    Returns:
        A tuple of beta1 and beta2 values.
    """
    beta1 = draw(st.floats(min_value=0.0, max_value=0.95, exclude_max=True, exclude_min=True))
    beta2 = draw(st.floats(min_value=beta1, max_value=0.999, exclude_max=True, exclude_min=True))
    return beta1, beta2


HYPERPARAM_OVERRIDE_STRATEGIES: Final[dict[str, st.SearchStrategy]] = {
    "lr": _ZERO_TO_ONE_FLOATS,
    "weight_decay": _ZERO_TO_ONE_FLOATS,
    "momentum": _ZERO_TO_ONE_FLOATS,
    "betas": betas(),
    "lr_decay": _ZERO_TO_ONE_FLOATS,
    "eps": _ZERO_TO_ONE_FLOATS,
    "centered": st.booleans(),
    "rho": _ZERO_TO_ONE_FLOATS,
    "momentum_decay": _ZERO_TO_ONE_FLOATS,
    "etas": st.tuples(
        st.floats(min_value=0.0, max_value=1.0, exclude_min=True, exclude_max=True),
        st.floats(min_value=1.0, max_value=2.0, exclude_min=True, exclude_max=True),
    ),
    "dampening": _ZERO_TO_ONE_FLOATS,
    "nesterov": st.booleans(),
    "initial_accumulator_value": _ZERO_TO_ONE_FLOATS,
}


def optimizer_type_strategy(
    allowed_optimizer_types: Sequence[type[torch.optim.Optimizer]] | None = None,
) -> st.SearchStrategy[type[torch.optim.Optimizer]]:
    """Strategy for generating torch optimizers.

    Args:
        allowed_optimizer_types: A sequence of optimizers to sample from. If None, all available optimizers are sampled.

    Returns:
        A strategy for generating torch optimizers.
    """
    if allowed_optimizer_types is None:
        allowed_optimizer_types = OPTIMIZERS
    return st.sampled_from(allowed_optimizer_types)


@st.composite
def optimizer_strategy(
    draw: st.DrawFn,
    optimizer_type: type[torch.optim.Optimizer] | st.SearchStrategy[type[torch.optim.Optimizer]] = None,
    **kwargs,
) -> st.SearchStrategy[OptimizerConstructorWithOnlyParameters]:
    """Strategy for generating torch optimizers.

    Args:
        draw: The draw function provided by `hypothesis`.
        optimizer_type: The optimizer type or a strategy for generating optimizer types.
        kwargs: Keyword arguments to pass to the optimizer constructor. If a keyword argument is a strategy, it will be
            drawn from.
    """
    if optimizer_type is None:
        optimizer_type = optimizer_type_strategy()
    if isinstance(optimizer_type, st.SearchStrategy):
        optimizer_type = draw(optimizer_type)

    sig = inspection_util.infer_signature_annotations(optimizer_type.__init__)
    for param in sig.parameters.values():
        if param.name in kwargs and isinstance(kwargs[param.name], st.SearchStrategy):
            kwargs[param.name] = draw(kwargs[param.name])
        elif param.annotation is inspect.Parameter.empty:
            continue
        elif param.name in HYPERPARAM_OVERRIDE_STRATEGIES:
            kwargs[param.name] = draw(HYPERPARAM_OVERRIDE_STRATEGIES[param.name])
        elif param.annotation in (float, int):
            kwargs[param.name] = draw(_ZERO_TO_ONE_FLOATS)
        else:
            kwargs[param.name] = draw(st.from_type(param.annotation))
    if "nesterov" in kwargs and kwargs["nesterov"] and "momentum" in kwargs:
        kwargs["dampening"] = 0
    kwargs.pop("self", None)  # Remove self if a type was inferred
    kwargs.pop("params", None)  # Remove params if a type was inferred

    hypothesis.note(f"Chosen optimizer type: {optimizer_type}")
    hypothesis.note(f"Chosen optimizer hyperparameters: {kwargs}")

    def optimizer_factory(params: Sequence[torch.nn.Parameter]) -> torch.optim.Optimizer:
        return optimizer_type(params, **kwargs)

    return optimizer_factory
