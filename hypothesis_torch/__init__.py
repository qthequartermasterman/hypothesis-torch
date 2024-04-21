__version__ = "0.1.0"
from hypothesis_torch.tensor import tensor_strategy
from hypothesis_torch.device import device_strategy
from hypothesis_torch.dtype import dtype_strategy
from hypothesis_torch.module import *

try:
    # Import Hugging Face strategies if transformers is installed
    import transformers
    from hypothesis_torch.huggingface import transformer_strategy
except ImportError:
    pass
