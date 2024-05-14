"""Strategies for generating Hugging Face transformers models."""

from __future__ import annotations

import inspect
from typing import Any, Callable, Final, TypeVar, cast

import hypothesis
import hypothesis.strategies as st
import torch
import transformers
import transformers.activations
import transformers.models
from typing_extensions import ParamSpec

from hypothesis_torch import inspection_util

P = ParamSpec("P")
T = TypeVar("T")
TransformerT = TypeVar("TransformerT", bound=transformers.PreTrainedModel)

_PLEASE_REPORT_ERROR: Final[str] = """\
Transformer {cls} is not officially supported.

If you encounter issues, please report them at https://github.com/qthequartermasterman/hypothesis-torch/issues."""

OFFICIALLY_SUPPORTED_TRANSFORMERS: Final[tuple[type[transformers.PreTrainedModel], ...]] = (
    transformers.LlamaPreTrainedModel,
    transformers.LlamaForCausalLM,
    transformers.MistralPreTrainedModel,
    transformers.MistralForCausalLM,
)

POSITIVE_INTS = st.integers(min_value=1, max_value=4)  # We intentionally limit positive ints for speed
FLOATS_BETWEEN_ZERO_AND_ONE = st.floats(
    min_value=0,
    max_value=1,
    allow_subnormal=False,
    allow_nan=False,
    allow_infinity=False,
)
FLOATS_GREATER_THAN_ZERO = st.floats(min_value=0, allow_subnormal=False, allow_nan=False, allow_infinity=False)
FLOATS_STRICTLY_GREATER_THAN_ZERO = st.floats(
    min_value=1e-6, allow_subnormal=False, allow_nan=False, allow_infinity=False, exclude_min=True
)
FLOATS_GREATER_THAN_ONE = st.floats(min_value=1, allow_subnormal=False, allow_nan=False, allow_infinity=False)


TRANSFORMER_CONFIG_KWARG_STRATEGIES = {
    "attention_bias": st.booleans(),
    "attention_dropout": FLOATS_BETWEEN_ZERO_AND_ONE,
    "bos_token_id": POSITIVE_INTS,
    "eos_token_id": POSITIVE_INTS,
    "hidden_act": st.sampled_from(["gelu", "relu", "silu", "gelu_new", "tanh"]),
    "activation": st.sampled_from(list(transformers.activations.ACT2FN.keys())),
    "activation_function": st.sampled_from(list(transformers.activations.ACT2FN.keys())),
    "projection_hidden_act": st.sampled_from(list(transformers.activations.ACT2FN.keys())),
    "hidden_size": POSITIVE_INTS,
    "initializer_factor": FLOATS_STRICTLY_GREATER_THAN_ZERO,
    "initializer_range": FLOATS_STRICTLY_GREATER_THAN_ZERO,
    "intermediate_size": POSITIVE_INTS,
    "max_position_embeddings": POSITIVE_INTS,
    "num_attention_heads": POSITIVE_INTS,
    "num_hidden_layers": POSITIVE_INTS,
    "rms_norm_eps": FLOATS_GREATER_THAN_ZERO,
    "pretrained_tp": POSITIVE_INTS,
    "rope_theta": FLOATS_GREATER_THAN_ZERO,
    "num_embeddings": POSITIVE_INTS,
    "vocab_size": POSITIVE_INTS,
    "num_key_value_heads": POSITIVE_INTS,
    "sliding_window": POSITIVE_INTS,
    "esmfold_config": st.just(
        transformers.models.esm.configuration_esm.EsmFoldConfig()
    ),  # TODO: Support arbitrary ESMfoldConfig
    "use_timm_backbone": st.just(False),  # TODO: Support timm_backbone
    "dropout": FLOATS_BETWEEN_ZERO_AND_ONE,
    "classifier_dropout_prob": FLOATS_BETWEEN_ZERO_AND_ONE,
    "attention_probs_dropout_prob": FLOATS_BETWEEN_ZERO_AND_ONE,
    "hidden_dropout_prob": FLOATS_BETWEEN_ZERO_AND_ONE,
    "summary_first_dropout": FLOATS_BETWEEN_ZERO_AND_ONE,
    "contrastive_hidden_size": POSITIVE_INTS,
    "init_std": FLOATS_STRICTLY_GREATER_THAN_ZERO,
    "key_dim": st.tuples(POSITIVE_INTS, POSITIVE_INTS, POSITIVE_INTS).map(list),
    "hidden_sizes": st.tuples(POSITIVE_INTS, POSITIVE_INTS, POSITIVE_INTS).map(list),
    "depths": st.tuples(POSITIVE_INTS, POSITIVE_INTS, POSITIVE_INTS).map(list),
    "mlp_ratio": st.tuples(POSITIVE_INTS, POSITIVE_INTS, POSITIVE_INTS).map(list),
    "attention_ratio": st.tuples(POSITIVE_INTS, POSITIVE_INTS, POSITIVE_INTS).map(list),
    "drop_path_rate": FLOATS_BETWEEN_ZERO_AND_ONE,
    "pooling": st.sampled_from(["mean", "max"]),
    "spec_size": st.one_of(POSITIVE_INTS, st.tuples(POSITIVE_INTS, POSITIVE_INTS)),
    "patch_stride": st.one_of(POSITIVE_INTS, st.tuples(POSITIVE_INTS, POSITIVE_INTS)),
    "img_size": st.one_of(POSITIVE_INTS, st.tuples(POSITIVE_INTS, POSITIVE_INTS)),
    "logit_scale_init_value": FLOATS_STRICTLY_GREATER_THAN_ZERO,
}


def ignore_errors(*errors_to_ignore: type[Exception]) -> Callable[[Callable[P, T]], Callable[P, T]]:
    """Decorator to ignore import errors."""

    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            try:
                return func(*args, **kwargs)
            except errors_to_ignore as e:
                hypothesis.note(f"Ignoring error: {e}")
                hypothesis.reject()

        return wrapper

    return decorator


@st.composite
def build_from_cls_init(
    draw: st.DrawFn,
    cls: type[T],
    **kwargs: Any,  # noqa: ANN401
) -> T:
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
        elif param.annotation is inspect.Parameter.empty:
            continue
        elif param.name in TRANSFORMER_CONFIG_KWARG_STRATEGIES:
            kwargs[param.name] = draw(TRANSFORMER_CONFIG_KWARG_STRATEGIES[param.name])
        elif "dropout" in param.name:
            kwargs[param.name] = draw(FLOATS_BETWEEN_ZERO_AND_ONE)
        elif param.annotation is int:
            kwargs[param.name] = draw(POSITIVE_INTS)
        else:
            kwargs[param.name] = draw(st.from_type(param.annotation))
    kwargs.pop("self", None)  # Remove self if a type was inferred

    # hidden_size must be divisible by num_heads
    if "hidden_size" in kwargs and "num_attention_heads" in kwargs:
        kwargs["hidden_size"] = kwargs["hidden_size"] * kwargs["num_attention_heads"]

    # pad_token_id must be less than vocab_size
    if "pad_token_id" in kwargs and "vocab_size" in kwargs:
        kwargs["pad_token_id"] = draw(st.integers(min_value=0, max_value=kwargs["vocab_size"] - 1))

    # Attention window (for LEDEncoder) must be even
    if "attention_window" in kwargs:
        kwargs["attention_window"] = kwargs["attention_window"] * 2

    # BridgeTowerConfig requires a `contrastive_hidden_size` parameter not included in its
    # TODO: Support BridgeTower

    # BitConfig requires a `layer_type` parameter of either "preactivation" or "bottleneck"
    if "Bit" in cls.__name__ and "layer_type" in kwargs:
        kwargs["layer_type"] = draw(st.sampled_from(["preactivation", "bottleneck"]))

    # Flaubert can only be used an encoder
    if "Flaubert" in cls.__name__ and "is_encoder" in kwargs:
        kwargs["is_encoder"] = True

    # Camembert can only be used as a decoder
    if "Camembert" in cls.__name__:
        kwargs["is_decoder"] = True

    # Flaubert requires pad_idx be less than n_words
    if "Flaubert" in cls.__name__:
        vocab_size = kwargs.get("vocab_size", kwargs.get("n_words"))
        kwargs["pad_index"] = draw(st.integers(min_value=0, max_value=vocab_size - 1))

    if "Levit" in cls.__name__:
        kwargs["num_attention_heads"] = (draw(st.tuples(POSITIVE_INTS, POSITIVE_INTS, POSITIVE_INTS).map(list)),)

    # Many models expect embed_dim to be divisible by num_heads
    classes_expecting_num_heads_and_embed_dim = [
        "Bark",
        "Blenderbot",
        "Bart",
        "BigBird",
    ]
    for class_name in classes_expecting_num_heads_and_embed_dim:
        if class_name in cls.__name__:
            if "num_heads" not in kwargs:
                kwargs["num_heads"] = draw(POSITIVE_INTS)
            if "embed_dim" not in kwargs:
                kwargs["embed_dim"] = draw(POSITIVE_INTS)
    if "embed_dim" in kwargs and "num_heads" in kwargs:
        kwargs["embed_dim"] = kwargs["embed_dim"] * kwargs["num_heads"]
    if "Bark" in cls.__name__ or "Bloom" in cls.__name__:
        if "hidden_size" not in kwargs:
            kwargs["hidden_size"] = draw(POSITIVE_INTS)
        kwargs["hidden_size"] = kwargs["hidden_size"] * kwargs["num_heads"]

    if "Camembert" in cls.__name__:
        kwargs["padding_idx"] = draw(st.integers(min_value=0, max_value=kwargs["num_embeddings"] - 1))

    if "BigBird" in cls.__name__:
        kwargs["attention_type"] = draw(st.sampled_from(["block_sparse", "original_full"]))

    # BitModel requires num_channels be divisible by num_groups
    if "Bit" in cls.__name__:
        kwargs["num_channels"] = kwargs["num_channels"] * kwargs["num_groups"]

    # Some models such as "CodeGen" have multiple Dropout probability parameters, each with "pdrop" in the name
    for key in kwargs:
        if "pdrop" in key:
            kwargs[key] = draw(FLOATS_BETWEEN_ZERO_AND_ONE)

    return cls(**kwargs)


@ignore_errors(ImportError, NotImplementedError)
@st.composite
def transformer_strategy(
    draw: st.DrawFn,
    cls: type[TransformerT] | st.SearchStrategy[type[TransformerT]],
    *,
    instantiate_weights: bool | st.SearchStrategy[bool] = True,
    **kwargs: Any,  # noqa: ANN401
) -> TransformerT:
    """Strategy for generating Hugging Face transformers.

    Args:
        draw: The draw function provided by `hypothesis`.
        cls: The transformer class to generate.
        instantiate_weights: Whether to instantiate the weights of the transformer. If False, the transformer will be
            instantiated on the meta device. This is useful for testing uses of transformers models that do not require
            a forward pass.
        kwargs: Keyword arguments to pass to the transformer constructor. If a keyword argument is a strategy, it will
            be drawn from.

    Raises:
        ValueError: If `instantiate_weights==False` on PyTorch<2, because the torch meta device cannot be used as a
            context manager.

    Returns:
        A strategy for generating Hugging Face transformers.
    """
    # TODO: Find a way to instantiate weights on the meta device in PyTorch<2.
    if not hasattr(torch.device("meta"), "__enter__"):  # pragma: no cover
        if instantiate_weights is False:
            raise ValueError(
                "Cannot instantiate weights on the meta device if the meta device context manager is not available.\n"
                "Please upgrade to PyTorch 2.0.0 or later."
            )
        if isinstance(instantiate_weights, st.SearchStrategy):
            instantiate_weights = instantiate_weights.filter(lambda x: x is True)

    if isinstance(cls, st.SearchStrategy):
        cls = draw(cls)

    if cls not in OFFICIALLY_SUPPORTED_TRANSFORMERS:
        hypothesis.note(_PLEASE_REPORT_ERROR.format(cls=cls))

    assert issubclass(cls, transformers.PreTrainedModel)
    hypothesis.note(f"Building transformer from {cls.__name__}")
    assert cls.config_class is not None
    config = draw(build_from_cls_init(cls.config_class, **kwargs))
    hypothesis.note(f"Building transformer ({cls.__name__}) with config {config}")

    if isinstance(instantiate_weights, st.SearchStrategy):
        instantiate_weights = draw(instantiate_weights)
    hypothesis.note(f"Instantiating weights: {instantiate_weights}")

    if instantiate_weights:
        return cast(TransformerT, cls(config))
    with torch.device("meta"):
        return cast(TransformerT, cls(config))
