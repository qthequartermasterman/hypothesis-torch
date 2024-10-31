"""Strategies for generating torch optimizers."""

from __future__ import annotations

import inspect
from collections.abc import Iterable, Sequence
from typing import Any, Callable, Final

import hypothesis
import torch.optim
from hypothesis import strategies as st
from typing_extensions import TypeAlias

from hypothesis_torch import inspection_util

# We do an alias here to avoid some type checking issues with torch 2.4.0
Optimizer: TypeAlias = torch.optim.Optimizer  # pyright: ignore[reportPrivateImportUsage]

OptimizerConstructorWithOnlyParameters: TypeAlias = Callable[[Iterable[torch.nn.Parameter]], Optimizer]

OPTIMIZERS: Final[tuple[type[Optimizer], ...]] = tuple(
    optimizer
    for optimizer in inspection_util.get_all_subclasses(Optimizer)
    if optimizer is not Optimizer and "NewCls" not in optimizer.__name__
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
    "fused": st.booleans() if torch.cuda.is_available() else st.just(False),
    "beta2_decay": st.floats(max_value=0.0, exclude_max=False, allow_nan=False, allow_infinity=False),
    "d": st.floats(min_value=1.0, exclude_min=False, allow_nan=False, allow_infinity=False),
}


def optimizer_type_strategy(
    allowed_optimizer_types: Sequence[type[Optimizer]] | None = None,
) -> st.SearchStrategy[type[Optimizer]]:
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
    optimizer_type: type[Optimizer] | st.SearchStrategy[type[Optimizer]] | None = None,
    **kwargs: Any,  # noqa: ANN401
) -> OptimizerConstructorWithOnlyParameters:
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

    # Adam cannot be both fused and differentiable simultaneously
    if "differentiable" in kwargs and kwargs["differentiable"] and "fused" in kwargs and kwargs["fused"]:
        kwargs.pop("differentiable")

    # Adafactor has a unique eps: Tuple[Optional[float], float], with eps[0] being None or >=0 and eps[1] >=0
    if "Adafactor" in optimizer_type.__name__:  # type: ignore
        eps0 = draw(st.one_of(st.none(), _ZERO_TO_ONE_FLOATS))
        kwargs["eps"] = (eps0, draw(_ZERO_TO_ONE_FLOATS))

    hypothesis.note(f"Chosen optimizer type: {optimizer_type}")
    hypothesis.note(f"Chosen optimizer hyperparameters: {kwargs}")

    def optimizer_factory(params: Iterable[torch.nn.Parameter]) -> Optimizer:
        return optimizer_type(params, **kwargs)

    return optimizer_factory
