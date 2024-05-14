[![PyPI version](https://img.shields.io/pypi/v/hypothesis-torch.svg)](https://pypi.org/project/hypothesis-torch) ![PyPI - Downloads](https://img.shields.io/pypi/dm/hypothesis-torch)
[![Checked with pyright](https://microsoft.github.io/pyright/img/pyright_badge.svg)](https://microsoft.github.io/pyright/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

# hypothesis-torch
Hypothesis strategies for various Pytorch structures (including tensors and modules).

[Hypothesis](https://hypothesis.readthedocs.io/en/latest/) is a powerful property-based testing library for Python. It
lacks built-in support for Pytorch tensors and modules, so this library provides strategies for generating them.

## Installation
`hypothesis-torch` can be installed via pip:
```bash
pip install hypothesis-torch
```

Optionally, you can also install the `huggingface` extra to also install the `transformers` library:
```bash
pip install hypothesis-torch[huggingface]
```

Strategies for generating Hugging Face transformer models are provided in the `hypothesis_torch.huggingface` module. If 
and only if `transformers` is installed when `hypothesis-torch` is imported, these strategies will be available from
the root `hypothesis_torch` module.

## What you can generate

### Tensors

Tensors can be generated with the `tensor_strategy` function. This function takes in optional arguments for the shape,
dtype, device, and other properties of the desired tensors. Each property can be specified as a fixed value or as a
strategy. For example, to generate a tensor with a shape of 3x3, a dtype of `torch.float32`, and values between 0 and 1,

```python
import hypothesis_torch
from hypothesis import strategies as st
import torch
hypothesis_torch.tensor_strategy(dtype=torch.float32, shape=(3, 3), elements=st.floats(0, 1))
```

Note that specifying other hypothesis strategies that return the same type as an argument will sample from that strategy
while generating the tensor. For example, to generate a tensor with any dtype, specify a strategy that returns a dtype:

```python
import hypothesis_torch
from hypothesis import strategies as st
import torch
hypothesis_torch.tensor_strategy(dtype=st.sampled_from([torch.float32, torch.float64]), shape=(3, 3), elements=st.floats(0, 1))
```

### Dtypes

Dtypes can be generated with the `dtype_strategy` function. If no arguments are provided, this function will default to 
sampling from the set of all Pytorch dtypes. 
    
```python
import hypothesis_torch
hypothesis_torch.dtype_strategy()
```

If a set of dtypes is provided, the function will sample from that set.

```python
import hypothesis_torch
import torch
hypothesis_torch.dtype_strategy(dtypes={torch.float32, torch.float64})
```

### Devices

Devices can be generated with the `device_strategy` function. If no arguments are provided, this function will default to
sampling from the set of all available, physical devices.

```python
import hypothesis_torch
hypothesis_torch.device_strategy()
```

If a set of devices is provided, the function will sample from that set.

```python
import hypothesis_torch
import torch
hypothesis_torch.device_strategy(devices={torch.device('cuda:0'), torch.device('cpu')})
```

If `allow_meta_device` is set to `True`, the strategy may also return meta devices, i.e. `torch.device('meta')`.

```python
import hypothesis_torch
hypothesis_torch.device_strategy(allow_meta_device=True)
```

### Modules

Various types of PyTorch modules have their own strategies.

#### Activation functions

Activation functions can be generated with the `same_shape_activation_strategy` function. 

```python
import hypothesis_torch
hypothesis_torch.same_shape_activation_strategy()
```

#### Fully-connected/Feed forward neural networks

Fully-connected neural networks can be generated with the `linear_network_strategy` function. This function takes in 
optional arguments for the input size, output size, and number of hidden layers. Each of these arguments can be 
specified as a fixed value or as a strategy. For example, to generate a fully-connected neural network with an input
size of 10, an output size of 5, and 3 hidden layers with sizes between 5 and 10:

```python
import hypothesis_torch
from hypothesis import strategies as st
hypothesis_torch.linear_network_strategy(input_shape=(1,10), output_shape=(1,5), hidden_layer_size=st.integers(5, 10), num_hidden_layers=3)
```

#### Hugging Face Transformer Models

Hugging Face transformer models can be generated with the `transformer_strategy` function. This function takes in any
Hugging Face `PreTrainedModel` subclass (or a strategy that generates references `PreTrainedModel` subclasses) and 
returns an instance of that model. For example, to generate an arbitrary Llama2 model:

```python
import hypothesis_torch
import transformers
hypothesis_torch.transformer_strategy(transformers.LlamaForCausalLM)
```

The strategy also accepts `kwargs` to pass to the model constructor. These can be either fixed values or strategies to 
generate those corresponding values. For example, to generate an arbitrary Llama2 model with a hidden size between 64 and
128, but a fixed vocabulary size of 1000:

```python
import hypothesis_torch
import transformers
from hypothesis import strategies as st
hypothesis_torch.transformer_strategy(transformers.LlamaForCausalLM, hidden_size=st.integers(64, 128), vocab_size=1000)
```

[! Note]
    Currently, the `transformer_strategy` only accepts `kwargs` that can be passed to the constructor of the model's 
    config class. Thus, it cannot currently replicate all the behavior of calling `from_pretrained` on a model class.
