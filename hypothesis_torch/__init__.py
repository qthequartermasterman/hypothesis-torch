"""Hypothesis strategies for various Pytorch structures (including tensors and modules).

[Hypothesis](https://hypothesis.readthedocs.io/en/latest/) is a powerful property-based testing library for Python. It
lacks built-in support for Pytorch tensors and modules, so this library provides strategies for generating them.
"""

__version__ = "0.6.1"
import importlib.util

from hypothesis_torch.device import (
    device_strategy,
    AVAILABLE_CPU_DEVICES,
    AVAILABLE_CUDA_DEVICES,
    AVAILABLE_MPS_DEVICES,
    AVAILABLE_META_DEVICES,
    AVAILABLE_PHYSICAL_DEVICES,
)
from hypothesis_torch.dtype import (
    dtype_strategy,
    FLOAT_DTYPES,
    INT_DTYPES,
    SIGNED_INT_DTYPES,
    UNSIGNED_INT_DTYPES,
    COMPLEX_DTYPES,
    BOOL_DTYPES,
    ALL_DTYPES,
)
from hypothesis_torch.layout import layout_strategy
from hypothesis_torch.memory_format import memory_format_strategy
from hypothesis_torch.module import linear_network_strategy, same_shape_activation_strategy
from hypothesis_torch.optim import optimizer_strategy, optimizer_type_strategy, OptimizerConstructorWithOnlyParameters
from hypothesis_torch.register_random_torch_state import TORCH_RANDOM_WRAPPER
from hypothesis_torch.tensor import tensor_strategy

__all__ = [
    "device_strategy",
    "dtype_strategy",
    "layout_strategy",
    "memory_format_strategy",
    "linear_network_strategy",
    "same_shape_activation_strategy",
    "optimizer_strategy",
    "optimizer_type_strategy",
    "OptimizerConstructorWithOnlyParameters",
    "tensor_strategy",
    "TORCH_RANDOM_WRAPPER",
    "AVAILABLE_CPU_DEVICES",
    "AVAILABLE_CUDA_DEVICES",
    "AVAILABLE_MPS_DEVICES",
    "AVAILABLE_META_DEVICES",
    "AVAILABLE_PHYSICAL_DEVICES",
    "FLOAT_DTYPES",
    "INT_DTYPES",
    "SIGNED_INT_DTYPES",
    "UNSIGNED_INT_DTYPES",
    "COMPLEX_DTYPES",
    "BOOL_DTYPES",
    "ALL_DTYPES",
]

if importlib.util.find_spec("transformers") is not None:
    # Import Hugging Face strategies if transformers is installed
    from hypothesis_torch.huggingface import transformer_strategy, OFFICIALLY_SUPPORTED_TRANSFORMERS

    __all__ += ["transformer_strategy", "OFFICIALLY_SUPPORTED_TRANSFORMERS"]
