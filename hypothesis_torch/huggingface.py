"""Strategies for generating Hugging Face transformers models."""

from __future__ import annotations

import inspect
from typing import TypeVar

import hypothesis.strategies as st
import torch
import transformers

from hypothesis_torch import inspection_util

T = TypeVar("T")
TransformerType = TypeVar("TransformerType", bound=transformers.PreTrainedModel)

POSITIVE_INTS = st.integers(min_value=1)
FLOATS_BETWEEN_ZERO_AND_ONE = st.floats(
    min_value=0,
    max_value=1,
    allow_subnormal=False,
    allow_nan=False,
    allow_infinity=False,
)
FLOATS_GREATER_THAN_ZERO = st.floats(min_value=0, allow_subnormal=False, allow_nan=False, allow_infinity=False)
FLOATS_GREATER_THAN_ONE = st.floats(min_value=1, allow_subnormal=False, allow_nan=False, allow_infinity=False)


TRANSFORMER_CONFIG_KWARG_STRATEGIES = {
    "attention_bias": st.booleans(),
    "attention_dropout": FLOATS_BETWEEN_ZERO_AND_ONE,
    "bos_token_id": POSITIVE_INTS,
    "eos_token_id": POSITIVE_INTS,
    "hidden_act": st.sampled_from(["gelu", "relu", "silu", "gelu_new", "tanh"]),
    "hidden_size": POSITIVE_INTS,
    "initializer_range": FLOATS_GREATER_THAN_ZERO,
    "intermediate_size": POSITIVE_INTS,
    "max_position_embeddings": POSITIVE_INTS,
    "num_attention_heads": POSITIVE_INTS,
    "num_hidden_layers": POSITIVE_INTS,
    "rms_norm_eps": FLOATS_GREATER_THAN_ZERO,
    "pretrained_tp": POSITIVE_INTS,
    "rope_theta": FLOATS_GREATER_THAN_ZERO,
}


@st.composite
def build_from_cls_init(draw: st.DrawFn, cls: type[T], **kwargs) -> T:
    """Strategy for generating instances of a class by drawing values for its constructor.

    Args:
        draw: The draw function provided by `hypothesis`.
        cls: The class to generate an instance of.
        kwargs: Keyword arguments to pass to the constructor. If a keyword argument is a strategy, it will be drawn
            from.

    Returns:
        An instance of the class.

    """
    sig = inspection_util.infer_signature_annotations(cls.__init__)
    for param in sig.parameters.values():
        if param.name in kwargs and isinstance(kwargs[param.name], st.SearchStrategy):
            kwargs[param.name] = draw(kwargs[param.name])
        if param.annotation is inspect.Parameter.empty:
            continue
        if param.name in TRANSFORMER_CONFIG_KWARG_STRATEGIES:
            kwargs[param.name] = draw(TRANSFORMER_CONFIG_KWARG_STRATEGIES[param.name])
        else:
            kwargs[param.name] = draw(st.from_type(param.annotation))
    kwargs.pop("self", None)  # Remove self if a type was inferred
    return cls(**kwargs)


@st.composite
def transformer_strategy(
    draw: st.DrawFn,
    cls: type[TransformerType] | st.SearchStrategy[type[TransformerType]],
    *,
    instantiate_weights: bool | st.SearchStrategy[bool] = True,
    **kwargs,
) -> TransformerType:
    """Strategy for generating Hugging Face transformers.

    Args:
        draw: The draw function provided by `hypothesis`.
        cls: The transformer class to generate.
        instantiate_weights: Whether to instantiate the weights of the transformer. If False, the transformer will be
            instantiated on the meta device. This is useful for testing uses of transformers models that do not require
            a forward pass.
        kwargs: Keyword arguments to pass to the transformer constructor. If a keyword argument is a strategy, it will
            be drawn from.

    Returns:
        A strategy for generating Hugging Face transformers.
    """
    if isinstance(cls, st.SearchStrategy):
        cls = draw(cls)
    assert issubclass(cls, transformers.PreTrainedModel)
    config = draw(build_from_cls_init(cls.config_class, **kwargs))

    if isinstance(instantiate_weights, st.SearchStrategy):
        instantiate_weights = draw(instantiate_weights)

    if instantiate_weights:
        return cls(config)
    with torch.device("meta"):
        return cls(config)
