"""Tests for the transformers strategies."""

import unittest
from types import ModuleType
from typing import Any

import hypothesis
import transformers
from hypothesis import strategies as st

import hypothesis_torch
from hypothesis_torch import inspection_util
from tests.unit import utils as test_utils

for module in transformers.models.__dict__.values():
    if type(module) is transformers.utils.import_utils._LazyModule:
        for attr in module._modules:
            if "modeling" in attr:
                getattr(module, attr)
    elif type(module) is ModuleType:
        print(module.__name__, module.__dict__)


TRANSFORMERS_TO_TEST: list[type[transformers.PreTrainedModel]] = inspection_util.get_all_subclasses(
    transformers.PreTrainedModel
)
# BridgeTower seems to be broken. It requires a `contrastive_hidden_size` parameter not included in its config.
# TODO: Support BridgeTower
# Align models, especially AlignVisionModel seem to keep crashing my tests due to memory.
# TODO: Support Align
_UNSUPPORTED_CLASSES = ["BridgeTower", "Align"]
TRANSFORMERS_TO_TEST = [m for m in TRANSFORMERS_TO_TEST if all(u not in m.__name__ for u in _UNSUPPORTED_CLASSES)]


class TestTransformers(unittest.TestCase):
    """Tests for transformers strategies."""

    @hypothesis.given(
        transformer_and_kwargs=test_utils.meta_strategy_constraints(
            strategy_func=hypothesis_torch.transformer_strategy,
            cls=st.sampled_from(TRANSFORMERS_TO_TEST),
        )
    )
    def test_transformers(self, transformer_and_kwargs: tuple[transformers.PreTrainedModel, dict[str, Any]]) -> None:
        """Test that the transformer is a LlamaForCausalLM."""
        transformer, kwargs = transformer_and_kwargs
        cls: type[transformers.PreTrainedModel] = kwargs["cls"]
        self.assertIsInstance(transformer, cls)
        # Should default to instantiated weights
        self.assertFalse(any(p.is_meta for p in transformer.parameters()))

    @hypothesis.given(
        transformer_and_kwargs=test_utils.meta_strategy_constraints(
            strategy_func=hypothesis_torch.transformer_strategy,
            cls=st.sampled_from(TRANSFORMERS_TO_TEST),
            instantiate_weights=False,
        )
    )
    def test_transformers_meta_device(
        self, transformer_and_kwargs: tuple[transformers.PreTrainedModel, dict[str, Any]]
    ) -> None:
        """Test that the transformer is a LlamaForCausalLM."""
        transformer, kwargs = transformer_and_kwargs

        cls: type[transformers.PreTrainedModel] = kwargs["cls"]
        self.assertIsInstance(transformer, cls)
        self.assertTrue(all(p.is_meta for p in transformer.parameters()))

    @hypothesis.given(transformer=hypothesis_torch.transformer_strategy(transformers.LlamaForCausalLM))
    def test_transformers_llama(self, transformer: transformers.LlamaForCausalLM) -> None:
        """Test that the transformer is a LlamaForCausalLM."""
        self.assertIsInstance(transformer, transformers.LlamaForCausalLM)
        # Should default to instantiated weights
        self.assertFalse(any(p.is_meta for p in transformer.parameters()))

    @hypothesis.given(
        transformer=hypothesis_torch.transformer_strategy(transformers.LlamaForCausalLM, instantiate_weights=False)
    )
    def test_transformers_meta_device_llama(self, transformer: transformers.LlamaForCausalLM) -> None:
        """Test that the transformer is a LlamaForCausalLM, with meta weights if instantiate weights is disabled."""
        self.assertIsInstance(transformer, transformers.LlamaForCausalLM)
        self.assertTrue(all(p.is_meta for p in transformer.parameters()))


# @pytest.mark.parametrize('transformer_type', TRANSFORMERS_TO_TEST)
# @hypothesis.given(
#     data=st.data()
# )
# def test_transformers(transformer_type:type[transformers.PreTrainedModel], data:st.DataObject) -> None:
#     """Test that the transformer strategy only generates valid items."""
#     transformer=data.draw(hypothesis_torch.transformer_strategy(transformer_type))
#     assert isinstance(transformer, transformer_type)
