__version__ = "0.1.7"
from hypothesis_torch.tensor import tensor_strategy
from hypothesis_torch.device import device_strategy
from hypothesis_torch.dtype import dtype_strategy
from hypothesis_torch.module import same_shape_activation_strategy, linear_network_strategy

# Import Hugging Face strategies if transformers is installed
import importlib.util
if importlib.util.find_spec("transformers") is not None:
    from hypothesis_torch.huggingface import transformer_strategy
