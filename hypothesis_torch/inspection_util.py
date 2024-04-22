"""Utility functions for inspecting and manipulating callables and classes signatures."""

from __future__ import annotations

import inspect
from typing import Callable, TypeVar

T = TypeVar("T")


class ParameterInferAnnotationsFromDefault(inspect.Parameter):
    """A parameter that infers the annotation from the default value if it is not specified.

    This is useful for inferring annotations for parameters that are missing annotations but have default values.
    """

    @property
    def annotation(self) -> type | inspect.Parameter.empty:
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
