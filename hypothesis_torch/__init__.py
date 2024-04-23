"""Hypothesis strategies for various Pytorch structures (including tensors and modules).

[Hypothesis](https://hypothesis.readthedocs.io/en/latest/) is a powerful property-based testing library for Python. It
lacks built-in support for Pytorch tensors and modules, so this library provides strategies for generating them.
"""

__version__ = "0.1.10"
import importlib.util

from hypothesis_torch.device import device_strategy
from hypothesis_torch.dtype import dtype_strategy
from hypothesis_torch.module import linear_network_strategy, same_shape_activation_strategy
from hypothesis_torch.tensor import tensor_strategy

if importlib.util.find_spec("transformers") is not None:
    # Import Hugging Face strategies if transformers is installed
    from hypothesis_torch.huggingface import transformer_strategy
