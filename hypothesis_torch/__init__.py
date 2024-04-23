"""Root imports for hypothesis-torch."""

__version__ = "0.1.10"
import importlib.util

from hypothesis_torch.device import device_strategy
from hypothesis_torch.dtype import dtype_strategy
from hypothesis_torch.module import linear_network_strategy, same_shape_activation_strategy
from hypothesis_torch.tensor import tensor_strategy

if importlib.util.find_spec("transformers") is not None:
    # Import Hugging Face strategies if transformers is installed
    from hypothesis_torch.huggingface import transformer_strategy
