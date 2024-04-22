from __future__ import annotations

from typing import TypeVar

import torch
from hypothesis import strategies as st
from torch import nn

from hypothesis_torch import utils

__all__ = [
    "same_shape_activation_strategy",
    "linear_network_strategy",
]

T = TypeVar("T")

SENSIBLE_FLOATS = st.floats(
    min_value=-10,
    max_value=10,
    allow_nan=False,
    allow_infinity=False,
    allow_subnormal=False,
)
SENSIBLE_POSITIVE_FLOATS = st.floats(
    min_value=0,
    max_value=10,
    allow_nan=False,
    allow_infinity=False,
    allow_subnormal=False,
)
POSITIVE_INTS = st.integers(min_value=1)


@st.composite
def signature_to_strategy(draw: st.DrawFn, constructor: type[T], *args, **kwargs) -> T:
    """Strategy for generating instances of a class by drawing values for its constructor.

    Args:
        draw: The draw function provided by `hypothesis`.
        constructor: The class to generate an instance of.
        args: Positional arguments to pass to the constructor. If an argument is a strategy, it will be drawn from.
        kwargs: Keyword arguments to pass to the constructor. If a keyword argument is a strategy, it will be drawn
            from.
    Returns:
        An instance of the class.
    """
    args_drawn = [draw(strategy) for strategy in args]
    kwargs_drawn = {k: draw(strategy) for k, strategy in kwargs.items()}
    return constructor(*args_drawn, **kwargs_drawn)


@st.composite
def hard_tanh_strategy(draw: st.DrawFn) -> nn.Hardtanh:
    """Strategy for generating instances of `nn.Hardtanh` by drawing values for its constructor.

    Args:
        draw: The draw function provided by `hypothesis`.

    Returns:
        An instance of `nn.Hardtanh`.
    """
    min_value = draw(SENSIBLE_FLOATS)
    max_value = draw(SENSIBLE_FLOATS.filter(lambda x: x > min_value))
    inplace = draw(st.booleans())
    return nn.Hardtanh(min_value, max_value, inplace)


def same_shape_activation_strategy() -> st.SearchStrategy[nn.Module]:
    """Strategy for generating activation functions that have the same shape input and output shape.

    Returns:
        A strategy for generating activation functions that have the same shape input and output shape.
    """
    return st.one_of(
        # The identity could be an activation function
        signature_to_strategy(nn.Identity),
        # nn.ELU(alpha:float, inplace:bool)
        # SENSIBLE_FLOATS.flatmap(lambda alpha: st.booleans().map(lambda inplace: nn.ELU(alpha, inplace))),
        signature_to_strategy(nn.ELU, alpha=SENSIBLE_FLOATS, inplace=st.booleans()),
        # nn.Hardshrink(lambd=0.5)
        # SENSIBLE_FLOATS.map(lambda lambd: nn.Hardshrink(lambd)),
        signature_to_strategy(nn.Hardshrink, lambd=SENSIBLE_FLOATS),
        # nn.Hardsigmoid(inplace=False)
        st.booleans().map(lambda inplace: nn.Hardsigmoid(inplace)),
        signature_to_strategy(nn.Hardsigmoid, inplace=st.booleans()),
        # nn.Hardtanh(min_val=-1.0, max_val=1.0, inplace=False)
        hard_tanh_strategy(),
        # nn.Hardswish
        signature_to_strategy(nn.Hardswish, inplace=st.booleans()),
        # nn.LeakyReLU(negative_slope=0.01, inplace=False)
        signature_to_strategy(nn.LeakyReLU, negative_slope=SENSIBLE_FLOATS, inplace=st.booleans()),
        # nn.LogSigmoid
        signature_to_strategy(nn.LogSigmoid),
        # TODO: nn.MultiheadAttention, although in the `Non-linear activations` section, does not have the same shape
        #  inside and outside
        # nn.PReLU(num_parameters=1, init=0.25, device=None, dtype=None)
        # TODO: PReLU might depend on the input shape
        # TODO: num_parameters (int) – number of a to learn. Although it takes an int as input, there is only two
        #  values are legitimate: 1, or the number of channels at input. Default: 1
        signature_to_strategy(nn.PReLU, num_parameters=st.just(1), init=SENSIBLE_FLOATS),
        # nn.ReLU
        signature_to_strategy(nn.ReLU, inplace=st.booleans()),
        # nn.ReLU6
        signature_to_strategy(nn.ReLU6, inplace=st.booleans()),
        # nn.RReLU
        signature_to_strategy(
            nn.RReLU,
            lower=SENSIBLE_FLOATS,
            upper=SENSIBLE_FLOATS,
            inplace=st.booleans(),
        ),
        # nn.SELU
        signature_to_strategy(nn.SELU, inplace=st.booleans()),
        # nn.CELU
        signature_to_strategy(nn.CELU, alpha=SENSIBLE_FLOATS, inplace=st.booleans()),
        # nn.GELU
        signature_to_strategy(nn.GELU, approximate=st.sampled_from(["none", "tanh"])),
        # nn.Sigmoid
        signature_to_strategy(nn.Sigmoid),
        # nn.SiLU
        signature_to_strategy(nn.SiLU, inplace=st.booleans()),
        # nn.Mish
        signature_to_strategy(nn.Mish, inplace=st.booleans()),
        # nn.Softplus
        signature_to_strategy(nn.Softplus, beta=SENSIBLE_FLOATS, threshold=POSITIVE_INTS),
        # nn.Softshrink
        signature_to_strategy(nn.Softshrink, lambd=SENSIBLE_POSITIVE_FLOATS),
        # nn.Softsign
        signature_to_strategy(nn.Softsign),
        # nn.Tanh
        signature_to_strategy(nn.Tanh),
        # nn.Tanhshrink
        signature_to_strategy(nn.Tanhshrink),
        # nn.Threshold
        signature_to_strategy(
            nn.Threshold,
            threshold=SENSIBLE_FLOATS,
            value=SENSIBLE_FLOATS,
            inplace=st.booleans(),
        ),
        # nn.GLU
        # TODO: GLU depends on the input shape
    )


@st.composite
def linear_network_strategy(
    draw: st.DrawFn,
    input_shape: tuple[int, ...] | torch.Size | st.SearchStrategy[tuple[int, ...]] | st.SearchStrategy[torch.Size],
    output_shape: tuple[int, ...] | torch.Size | st.SearchStrategy[tuple[int, ...]] | st.SearchStrategy[torch.Size],
    activation_layer: nn.Module | st.SearchStrategy[nn.Module],
    hidden_layer_size: int | st.SearchStrategy[int],
    depth: int | st.SearchStrategy[int],
    device: torch.device | st.SearchStrategy[torch.device],
) -> nn.Module:
    """Strategy for generating random Torch fully-connected networks (sequential networks of linear layers with
    activation functions).

    Args:
        draw: The draw function provided by `hypothesis`.
        input_shape: The shape of the input tensor. If a strategy is provided, it will be drawn from.
        output_shape: The shape of the output tensor. If a strategy is provided, it will be drawn from.
        activation_layer: Activation layer to use. If a strategy is provided, it will be drawn from.
        hidden_layer_size: The size of the hidden layers. If a strategy is provided, it will be drawn from.
        depth: The maximum depth of the network. If a strategy is provided, it will be drawn from.
        device: The device on which to place the network. If a strategy is provided, it will be drawn from.

    Returns:
        A strategy for generating random linear networks.
    """
    if isinstance(input_shape, st.SearchStrategy):
        input_shape = draw(input_shape)
    if len(input_shape) not in {1, 2}:
        raise ValueError(f"input_shape must be a 1D or 2D tuple, but got {input_shape}")
    *_, input_size = input_shape

    if isinstance(output_shape, st.SearchStrategy):
        output_shape = draw(output_shape)
    if len(output_shape) not in {1, 2}:
        raise ValueError(f"output_shape must be a 1D or 2D tuple, but got {output_shape}")
    *_, output_size = output_shape

    if isinstance(device, st.SearchStrategy):
        device = draw(device)

    if isinstance(activation_layer, nn.Module):
        activation_layer_strategy = st.just(activation_layer)
    else:
        activation_layer_strategy = activation_layer

    if not isinstance(hidden_layer_size, st.SearchStrategy):
        hidden_layer_size = st.just(hidden_layer_size)
    if isinstance(depth, st.SearchStrategy):
        depth = draw(depth)

    with device:
        interior_layer_sizes = draw(
            st.lists(
                hidden_layer_size,
                min_size=depth,
                max_size=depth,
            )
        )
        layer_sizes = [input_size, *interior_layer_sizes, output_size]
        layers: list[nn.Module] = [nn.Linear(a, b) for a, b in utils.pairwise(layer_sizes)]
        activations: list[nn.Module] = draw(
            st.lists(activation_layer_strategy, min_size=len(layers), max_size=len(layers))
        )
        return nn.Sequential(*utils.alternate(layers, activations))


def convolution_output_shape(
    input_shape: tuple[int, ...] | torch.Tensor,
    kernel_size: tuple[int, ...] | torch.Tensor,
    stride: tuple[int, ...] | torch.Tensor,
    padding: tuple[int, ...] | torch.Tensor,
    dilation: tuple[int, ...] | torch.Tensor,
) -> tuple[int, ...]:
    """Calculate the output shape of a convolutional layer."""
    input_shape = torch.tensor(input_shape, dtype=torch.uint8)
    kernel_size = torch.tensor(kernel_size, dtype=torch.uint8)
    stride = torch.tensor(stride, dtype=torch.uint8)
    padding = torch.tensor(padding, dtype=torch.uint8)
    dilation = torch.tensor(dilation, dtype=torch.uint8)
    return tuple(torch.floor((input_shape + 2 * padding - dilation * (kernel_size - 1) - 1) / stride + 1).tolist())
