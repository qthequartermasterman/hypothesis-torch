"""Hypothesis strategies for various Pytorch structures (including tensors and modules).

[Hypothesis](https://hypothesis.readthedocs.io/en/latest/) is a powerful property-based testing library for Python. It
lacks built-in support for Pytorch tensors and modules, so this library provides strategies for generating them.
"""

__version__ = "2.0.0"
import importlib.util

from hypothesis_torch.device import (
    cuda_devices,
    device_strategy,
    mps_devices,
    not_mps_devices,
    physical_devices,
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
    "BOOL_DTYPES",
    "COMPLEX_DTYPES",
    "FLOAT_DTYPES",
    "INT_DTYPES",
    "SIGNED_INT_DTYPES",
    "TORCH_RANDOM_WRAPPER",
    "UNSIGNED_INT_DTYPES",
    "OptimizerConstructorWithOnlyParameters",
    "cuda_devices",
    "device_strategy",
    "dtype_strategy",
    "layout_strategy",
    "linear_network_strategy",
    "memory_format_strategy",
    "mps_devices",
    "not_mps_devices",
    "optimizer_strategy",
    "optimizer_type_strategy",
    "physical_devices",
    "same_shape_activation_strategy",
    "tensor_strategy",
]

if importlib.util.find_spec("transformers") is not None:
    # Import Hugging Face strategies if transformers is installed
    from hypothesis_torch.huggingface import OFFICIALLY_SUPPORTED_TRANSFORMERS, transformer_strategy

    __all__ += ["OFFICIALLY_SUPPORTED_TRANSFORMERS", "transformer_strategy"]
