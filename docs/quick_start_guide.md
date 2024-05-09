# Quick Start Guide

`hypothesis-torch` is a package of `hypothesis` strategies for various Pytorch structures (including tensors and modules).

## What is `hypothesis` and property-based testing?
In short, property-based testing is a testing methodology where the developer defined properties a unit of code should have, and the testing framework generates arbitrary inputs (following the developer's guidelines) to test the code against these properties. This is in contrast to example-based testing, where the developer provides specific inputs and expected outputs. This is exceptionally useful for (but by no means limited to!) [NP-class problems](https://en.wikipedia.org/wiki/NP_(complexity)) where solving is difficult, but checking a solution is easy. 

[Hypothesis](https://hypothesis.readthedocs.io/en/latest/) is a powerful property-based testing library for Python. It
lacks built-in support for Pytorch tensors and modules, so this library provides strategies for generating them.

The [`hypothesis` quick start guide](https://hypothesis.readthedocs.io/en/latest/quickstart.html) is a great place to start if you're new to property-based testing.

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

## An example with tensors

Suppose we have written a function that takes two PyTorch tensors, and [projects](https://en.wikipedia.org/wiki/Vector_projection) the second one onto the first one (treating all tensors as vectors).

We consequently want to define our function to have the following properties (which constitute one definition of a vector projection):
    1. The projection (output tensor) should all be parallel to the first input tensor.
    2. The second input tensor subtracted by the projection should be orthogonal to the first input tensor.

We might use these properties to define a test for our function. We can use `hypothesis-torch` to generate random tensors to test our function against these properties.

In the sample below, the two tensors will be in single precision (`torch.float32`) and have a shape of `(1, 2, 3)`, but these values could be changed to any valid values for the `dtype`, `shape`.

```python
import torch
import hypothesis_torch
from hypothesis import given
from hypothesis import strategies as st

def project(tensor1: torch.Tensor, tensor2: torch.Tensor) -> torch.Tensor:
    """Project tensor2 onto tensor1."""
    return tensor2.dot(tensor1) / tensor1.dot(tensor1) * tensor1

@given(
    tensor1=hypothesis_torch.tensor_strategy(
        dtype=torch.float32,
        shape=(1,2,3),
    ), 
    tensor2=hypothesis_torch.tensor_strategy(
        dtype=torch.float32,
        shape=(1,2,3),
    ),
)
def test_projection(tensor1: torch.Tensor, tensor2: torch.Tensor):
    projection = project(tensor1, tensor2)
    # Property 1
    # The projection (output tensor) should all be parallel to the first input tensor.
    # Two vectors are parallel if and only if their cosine similarity is 1.
    assert torch.allclose(torch.nn.functional.cosine_similarity(projection, tensor1), torch.tensor(1.0))
    
    # Property 2
    # The second input tensor subtracted by the projection should be orthogonal to the first input tensor.
    # Two vectors are orthogonal if and only if their dot product is 0.
    difference = tensor2 - projection
    assert torch.allclose(difference.dot(tensor1), torch.tensor(0.0))
```

Our test does not require any knowledge of the implementation of `project`, nor does it require any specific examples of input tensors. 
Instead, it generates random tensors and tests the function against the properties we defined. `hypothesis` will use the `tensor_strategy`
to attempt to find a counterexample to our properties. If it finds one, it will shrink the input tensors to the smallest possible example 
that violates the properties.

Very quickly, however, `hypothesis` will inform us that our function fails (will raise an division by zero error) for the example `torch.Tensor([[[0,0,0],[0,0,0]]])`. 
This should be expected, however, because the projection of any vector onto the zero vector is undefined. In this case, we should add a hypothesis assume to ensure that the first tensor is not the zero tensor.

```python
import torch
import hypothesis_torch
from hypothesis import given, assume

def project(tensor1: torch.Tensor, tensor2: torch.Tensor) -> torch.Tensor:
    """Project tensor2 onto tensor1."""
    return tensor2.dot(tensor1) / tensor1.dot(tensor1) * tensor1

@given(
    tensor1=hypothesis_torch.tensor_strategy(
        dtype=torch.float32,
        shape=(1,2,3),
    ), 
    tensor2=hypothesis_torch.tensor_strategy(
        dtype=torch.float32,
        shape=(1,2,3),
    ),
)
def test_projection(tensor1: torch.Tensor, tensor2: torch.Tensor):

    # Assume that the first tensor is not the zero tensor, because the projection of any vector onto the zero vector is undefined.
    # We have to use a small epsilon value because the values are floats and we can still have numerical instability close to 0 vectors.
    assume(tensor1.norm().item() > 1e-6)
    
    projection = project(tensor1, tensor2)
    # Property 1
    # The projection (output tensor) should all be parallel to the first input tensor.
    # Two vectors are parallel if and only if their cosine similarity is 1.
    assert torch.allclose(torch.nn.functional.cosine_similarity(projection, tensor1), torch.tensor(1.0))
    
    # Property 2
    # The second input tensor subtracted by the projection should be orthogonal to the first input tensor.
    # Two vectors are orthogonal if and only if their dot product is 0.
    difference = tensor2 - projection
    assert torch.allclose(difference.dot(tensor1), torch.tensor(0.0))
```
