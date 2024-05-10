"""Tests for the transformers strategies."""

import contextlib
import os
from types import ModuleType
from typing import Final

import hypothesis
import pytest
import transformers
from hypothesis import strategies as st

import hypothesis_torch
from hypothesis_torch import inspection_util

_TEST_UNSUPPORTED_TRANSFORMERS_SKIP_REASON: Final[str] = """\
Skipping unsupported transformers. To test unsupported transformers, please set the environment variable \
HYPOTHESIS_TORCH_TEST_UNSUPPORTED_TRANSFORMERS to `True`."""

TEST_UNSUPPORTED_TRANSFORMERS: Final[bool] = (
    os.getenv("HYPOTHESIS_TORCH_TEST_UNSUPPORTED_TRANSFORMERS", "False").lower() == "true"
)


@pytest.mark.parametrize("instantiate_weights", [True, False])
@pytest.mark.parametrize("transformer_type", hypothesis_torch.OFFICIALLY_SUPPORTED_TRANSFORMERS)
@hypothesis.given(data=st.data())
@hypothesis.settings(deadline=None)
def test_officially_supported_transformers(
    instantiate_weights: bool, transformer_type: type[transformers.PreTrainedModel], data: st.DataObject
) -> None:
    """Test that the transformer strategy only generates valid items."""
    transformer = data.draw(
        hypothesis_torch.transformer_strategy(transformer_type, instantiate_weights=instantiate_weights)
    )
    assert isinstance(transformer, transformer_type)


# We will dynamically test all available transformers models.
for module in transformers.models.__dict__.values():
    with contextlib.suppress(ImportError):
        if type(module) is transformers.utils.import_utils._LazyModule:
            for attr in module._modules:
                if "modeling" in attr:
                    getattr(module, attr)
        elif type(module) is ModuleType:
            print(module.__name__, module.__dict__)

AVAILABLE_TRANSFORMERS: list[type[transformers.PreTrainedModel]] = inspection_util.get_all_subclasses(
    transformers.PreTrainedModel
)
# BridgeTower seems to be broken. It requires a `contrastive_hidden_size` parameter not included in its config.
# TODO: Support BridgeTower
# Align models, especially AlignVisionModel seem to keep crashing my tests due to memory.
# TODO: Support Align
# "Alt" models seem to have issues I haven't diagnosed yet.
# TODO: Support Alt
# "Autoformer" models require specifying "prediction_length" in their config.
# TODO: Support Autoformer
# "Beit" models are giving me issues with "NotImplementedErrors" on meta devices.
# TODO: Support Beit
# Some "Clap" models are giving NotImplementedErrors and some others are giving:
#   |   File "/.../site-packages/transformers/models/clap/modeling_clap.py", line 826, in __init__
#   |     self.freq_ratio = config.spec_size // config.num_mel_bins
#   | TypeError: unsupported operand type(s) for //: 'tuple' and 'int'
# TODO: Support Clap
# "Clvp" is giving errors about "vocab_size" not being an attribute
# TODO: Support Clvp
# "ConditionalDetr" is giving errors about pretrained backbone weights
_UNSUPPORTED_CLASSES = ["BridgeTower", "Align", "Alt", "Autoformer", "Beit", "Clap", "Clvp", "ConditionalDetr"]
POTENTIALLY_SUPPORTED_TRANSFORMERS = [
    m for m in AVAILABLE_TRANSFORMERS if all(u not in m.__name__ for u in _UNSUPPORTED_CLASSES)
]


# Because there are A LOT of these models, and we need to test them all, we will reduce the time needed to test them by
# not instantiating the weights.
@pytest.mark.parametrize("instantiate_weights", [False])
@pytest.mark.parametrize("transformer_type", POTENTIALLY_SUPPORTED_TRANSFORMERS)
@hypothesis.given(data=st.data())
def test_unofficially_supported_transformers(
    instantiate_weights: bool, transformer_type: type[transformers.PreTrainedModel], data: st.DataObject
) -> None:
    """Test that the transformer strategy only generates valid items."""
    # For some reason, using a skipif decorator doesn't work here.
    if not TEST_UNSUPPORTED_TRANSFORMERS:
        pytest.skip(_TEST_UNSUPPORTED_TRANSFORMERS_SKIP_REASON)
    transformer = data.draw(
        hypothesis_torch.transformer_strategy(transformer_type, instantiate_weights=instantiate_weights)
    )
    assert isinstance(transformer, transformer_type)
