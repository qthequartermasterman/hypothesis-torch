"""Strategies for generating PyTorch Modules."""

from __future__ import annotations

import contextlib
from collections.abc import Sequence
from itertools import starmap
from typing import TypeVar

import torch
from hypothesis import strategies as st
from torch import nn

from hypothesis_torch import inspection_util, utils

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


def _context_manager(device: torch.device) -> torch.device | contextlib.nullcontext:
    """Return a context manager for the device.

    For torch>=2, this is a no-op. The default device will bet set to the `device` inside the returned context.
    For torch<2, however, this returns an empty context manager. No default device will be set. Consequently, manual
    casting will be necessary at the end of the context.

    Args:
        device: The device to use.

    Returns:
        A context manager for the device.
    """
    return device if hasattr(device, "__enter__") else contextlib.nullcontext()


@st.composite
def lower_upper_strategy(draw: st.DrawFn) -> tuple[float, float]:
    """Strategy for generating a pair of floats where the first is less than the second.

    Args:
        draw: The draw function provided by `hypothesis`.

    Returns:
        A pair of floats where the first is less than the second.

    """
    lower = draw(SENSIBLE_FLOATS)
    upper = draw(SENSIBLE_FLOATS.filter(lambda x: x > lower))
    return lower, upper


@st.composite
def rrelu_strategy(draw: st.DrawFn) -> nn.RReLU:
    """Strategy for generating instances of `nn.RReLU` by drawing values for its constructor.

    Args:
        draw: The draw function provided by `hypothesis`.

    Returns:
        An instance of `nn.RReLU`.
    """
    lower, upper = draw(lower_upper_strategy())
    inplace = draw(st.booleans())
    return nn.RReLU(lower, upper, inplace)


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


activation_strategies: dict[type[nn.Module], st.SearchStrategy[nn.Module]] = {
    nn.Identity: inspection_util.signature_to_strategy(nn.Identity),
    nn.ELU: inspection_util.signature_to_strategy(nn.ELU, alpha=SENSIBLE_FLOATS, inplace=st.booleans()),
    nn.Hardshrink: inspection_util.signature_to_strategy(nn.Hardshrink, lambd=SENSIBLE_FLOATS),
    nn.Hardsigmoid: inspection_util.signature_to_strategy(nn.Hardsigmoid, inplace=st.booleans()),
    nn.Hardtanh: hard_tanh_strategy(),
    nn.Hardswish: inspection_util.signature_to_strategy(nn.Hardswish, inplace=st.booleans()),
    nn.LeakyReLU: inspection_util.signature_to_strategy(
        nn.LeakyReLU, negative_slope=SENSIBLE_FLOATS, inplace=st.booleans()
    ),
    nn.LogSigmoid: inspection_util.signature_to_strategy(nn.LogSigmoid),
    # TODO: nn.MultiheadAttention, although in the `Non-linear activations` section, does not have the same shape
    #  inside and outside
    # TODO: nn.PReLU(num_parameters=1, init=0.25, device=None, dtype=None)
    # TODO: PReLU might depend on the input shape
    # TODO: num_parameters (int) -- number of a to learn. Although it takes an int as input, there is only two
    #  values are legitimate: 1, or the number of channels at input. Default: 1
    nn.PReLU: inspection_util.signature_to_strategy(nn.PReLU, num_parameters=st.just(1), init=SENSIBLE_FLOATS),
    nn.ReLU: inspection_util.signature_to_strategy(nn.ReLU, inplace=st.booleans()),
    nn.ReLU6: inspection_util.signature_to_strategy(nn.ReLU6, inplace=st.booleans()),
    nn.RReLU: rrelu_strategy(),
    nn.SELU: inspection_util.signature_to_strategy(nn.SELU, inplace=st.booleans()),
    nn.CELU: inspection_util.signature_to_strategy(
        nn.CELU, alpha=SENSIBLE_FLOATS.filter(lambda x: abs(x) > 1e-5), inplace=st.booleans()
    ),
    nn.GELU: inspection_util.signature_to_strategy(nn.GELU, approximate=st.sampled_from(["none", "tanh"])),
    nn.Sigmoid: inspection_util.signature_to_strategy(nn.Sigmoid),
    nn.SiLU: inspection_util.signature_to_strategy(nn.SiLU, inplace=st.booleans()),
    nn.Mish: inspection_util.signature_to_strategy(nn.Mish, inplace=st.booleans()),
    nn.Softplus: inspection_util.signature_to_strategy(
        nn.Softplus, beta=SENSIBLE_FLOATS, threshold=SENSIBLE_POSITIVE_FLOATS
    ),
    nn.Softshrink: inspection_util.signature_to_strategy(nn.Softshrink, lambd=SENSIBLE_POSITIVE_FLOATS),
    nn.Softsign: inspection_util.signature_to_strategy(nn.Softsign),
    nn.Tanh: inspection_util.signature_to_strategy(nn.Tanh),
    nn.Tanhshrink: inspection_util.signature_to_strategy(nn.Tanhshrink),
    nn.Threshold: inspection_util.signature_to_strategy(
        nn.Threshold, threshold=SENSIBLE_FLOATS, value=SENSIBLE_FLOATS, inplace=st.booleans()
    ),
    # TODO: nn.GLU depends on the input shape
}


def same_shape_activation_strategy(
    allowed_activation_functions: Sequence[type[nn.Module]] | Sequence[st.SearchStrategy[nn.Module]] | None = None,
) -> st.SearchStrategy[nn.Module]:
    """Strategy for generating activation functions that have the same shape input and output shape.

    Args:
        allowed_activation_functions: Activation functions to sample from.
            - If a sequence of strategies is provided, only these strategies are sampled from.
            - If a sequence of module types is provided, the elements are the activation functions to sample from.
            - If `None`, all supported activation functions are sampled.
            - For `None` or sequence of module type inputs, see complete list of supported activation functions in
            `activation_strategies`.

    Returns:
        A strategy for generating activation functions that have the same shape input and output shape.
    """
    if allowed_activation_functions is None:
        allowed_activation_functions = list(activation_strategies.keys())
    assert allowed_activation_functions is not None
    strategies: list[st.SearchStrategy[nn.Module]] = []
    for activation_function in allowed_activation_functions:
        if isinstance(activation_function, st.SearchStrategy):
            strategies.append(activation_function)
        elif activation_function in activation_strategies:
            strategies.append(activation_strategies[activation_function])
        else:
            raise ValueError(f"Unsupported activation function: {activation_function}")
    return st.one_of(strategies)


@st.composite
def linear_network_strategy(
    draw: st.DrawFn,
    input_shape: tuple[int, ...] | torch.Size | st.SearchStrategy[tuple[int, ...]] | st.SearchStrategy[torch.Size],
    output_shape: tuple[int, ...] | torch.Size | st.SearchStrategy[tuple[int, ...]] | st.SearchStrategy[torch.Size],
    activation_layer: nn.Module | st.SearchStrategy[nn.Module],
    hidden_layer_size: int | st.SearchStrategy[int],
    num_hidden_layers: int | st.SearchStrategy[int],
    device: torch.device | st.SearchStrategy[torch.device],
) -> nn.Module:
    """Strategy for generating random Torch sequential networks of linear layers with activation functions.

    Args:
        draw: The draw function provided by `hypothesis`.
        input_shape: The shape of the input tensor. If a strategy is provided, it will be drawn from.
        output_shape: The shape of the output tensor. If a strategy is provided, it will be drawn from.
        activation_layer: Activation layer to use. If a strategy is provided, it will be drawn from.
        hidden_layer_size: The size of the hidden layers. If a strategy is provided, it will be drawn from.
        num_hidden_layers: The maximum depth of the network. If a strategy is provided, it will be drawn from.
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

    if not isinstance(activation_layer, st.SearchStrategy):
        activation_layer_strategy = st.just(activation_layer)
    else:
        activation_layer_strategy = activation_layer

    # Several activation functions are not supported on MPS devices
    if device.type == "mps":
        unsupported_mps_activations = [nn.Hardshrink, nn.RReLU]

        activation_layer_strategy = activation_layer_strategy.filter(
            lambda x: not isinstance(x, tuple(unsupported_mps_activations))
        )

    if not isinstance(hidden_layer_size, st.SearchStrategy):
        hidden_layer_size = st.just(hidden_layer_size)
    if isinstance(num_hidden_layers, st.SearchStrategy):
        num_hidden_layers = draw(num_hidden_layers)

    with _context_manager(device):
        interior_layer_sizes = draw(
            st.lists(
                hidden_layer_size,
                min_size=num_hidden_layers,
                max_size=num_hidden_layers,
            )
        )
        layer_sizes = [input_size, *interior_layer_sizes, output_size]
        layers: list[nn.Module] = list(starmap(nn.Linear, utils.pairwise(layer_sizes)))
        activations: list[nn.Module] = draw(
            st.lists(activation_layer_strategy, min_size=len(layers), max_size=len(layers)),
        )
        return nn.Sequential(*utils.alternate(layers, activations)).to(device)


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
