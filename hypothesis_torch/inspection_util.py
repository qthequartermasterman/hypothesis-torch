"""Utility functions for inspecting and manipulating callables and classes signatures."""

from __future__ import annotations

import inspect
from typing import Any, Callable, TypeVar

import torch
from hypothesis import strategies as st

T = TypeVar("T")


class ParameterInferAnnotationsFromDefault(inspect.Parameter):
    """A parameter that infers the annotation from the default value if it is not specified.

    This is useful for inferring annotations for parameters that are missing annotations but have default values.
    """

    # mypy does like like the fact that `inspect.Parameter.empty` is a variable pointing to a class.
    @property
    def annotation(self) -> type | inspect.Parameter.empty:  # type: ignore[valid-type]
        """Get the annotation of the parameter, inferring it from the default value if it is not specified.

        Returns:
            The annotation (specified or inferred) of the parameter.

        """
        super_annotation = super().annotation
        if super_annotation is not inspect.Parameter.empty:
            return super_annotation
        if self.default is inspect.Parameter.empty:
            return inspect.Parameter.empty
        return type(self.default)


def infer_signature_annotations(func: Callable) -> inspect.Signature:
    """Get a signature of a callable, inferring missing annotations from default values."""
    sig = inspect.signature(func)
    new_params = []
    for param in sig.parameters.values():
        new_param = ParameterInferAnnotationsFromDefault(
            name=param.name,
            kind=param.kind,
            default=param.default,
        )
        new_params.append(new_param)
    return sig.replace(parameters=new_params)


def get_all_subclasses(cls: type[T]) -> list[type[T]]:
    """Get all subclasses (including descendants) of a class.

    Args:
        cls: The class to get the subclasses of.

    Returns:
        A list of all subclasses of the class.

    """
    all_subclasses = []
    for subclass in cls.__subclasses__():
        all_subclasses.append(subclass)
        all_subclasses.extend(get_all_subclasses(subclass))
    return all_subclasses


@st.composite
def signature_to_strategy(
    draw: st.DrawFn,
    constructor: type[T],
    *args: Any,  # noqa: ANN401
    **kwargs: Any,  # noqa: ANN401
) -> T:
    """Strategy for generating instances of a class by drawing values for its constructor.

    Args:
        draw: The draw function provided by `hypothesis`.
        constructor: The class to generate an instance of.
        args: Positional arguments to pass to the constructor. If an argument is a strategy, it will be drawn from.
        kwargs: Keyword arguments to pass to the constructor. If a keyword argument is a strategy, it will be drawn
            from.

    Returns:
        An instance of the class.

    """
    args_drawn = [draw(strategy) for strategy in args]
    kwargs_drawn = {k: draw(strategy) for k, strategy in kwargs.items()}
    return constructor(*args_drawn, **kwargs_drawn)
