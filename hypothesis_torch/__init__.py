"""Hypothesis strategies for various Pytorch structures (including tensors and modules).

[Hypothesis](https://hypothesis.readthedocs.io/en/latest/) is a powerful property-based testing library for Python. It
lacks built-in support for Pytorch tensors and modules, so this library provides strategies for generating them.
"""

__version__ = "0.9.2"
import importlib.util

from hypothesis_torch.device import (
    AVAILABLE_CPU_DEVICES,
    AVAILABLE_CUDA_DEVICES,
    AVAILABLE_META_DEVICES,
    AVAILABLE_MPS_DEVICES,
    AVAILABLE_PHYSICAL_DEVICES,
    device_strategy,
)
from hypothesis_torch.dtype import (
    ALL_DTYPES,
    BOOL_DTYPES,
    COMPLEX_DTYPES,
    FLOAT_DTYPES,
    INT_DTYPES,
    SIGNED_INT_DTYPES,
    UNSIGNED_INT_DTYPES,
    dtype_strategy,
)
from hypothesis_torch.layout import layout_strategy
from hypothesis_torch.memory_format import memory_format_strategy
from hypothesis_torch.module import linear_network_strategy, same_shape_activation_strategy
from hypothesis_torch.optim import OptimizerConstructorWithOnlyParameters, optimizer_strategy, optimizer_type_strategy
from hypothesis_torch.register_random_torch_state import TORCH_RANDOM_WRAPPER
from hypothesis_torch.tensor import tensor_strategy

__all__ = [
    "ALL_DTYPES",
    "AVAILABLE_CPU_DEVICES",
    "AVAILABLE_CUDA_DEVICES",
    "AVAILABLE_META_DEVICES",
    "AVAILABLE_MPS_DEVICES",
    "AVAILABLE_PHYSICAL_DEVICES",
    "BOOL_DTYPES",
    "COMPLEX_DTYPES",
    "FLOAT_DTYPES",
    "INT_DTYPES",
    "SIGNED_INT_DTYPES",
    "TORCH_RANDOM_WRAPPER",
    "UNSIGNED_INT_DTYPES",
    "OptimizerConstructorWithOnlyParameters",
    "device_strategy",
    "dtype_strategy",
    "layout_strategy",
    "linear_network_strategy",
    "memory_format_strategy",
    "optimizer_strategy",
    "optimizer_type_strategy",
    "same_shape_activation_strategy",
    "tensor_strategy",
]

if importlib.util.find_spec("transformers") is not None:
    # Import Hugging Face strategies if transformers is installed
    from hypothesis_torch.huggingface import OFFICIALLY_SUPPORTED_TRANSFORMERS, transformer_strategy

    __all__ += ["OFFICIALLY_SUPPORTED_TRANSFORMERS", "transformer_strategy"]
