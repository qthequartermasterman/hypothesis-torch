"""Strategies for generating PyTorch modules."""

import unittest
from typing import Any

import hypothesis
import torch
from hypothesis import strategies as st

import hypothesis_torch
from tests.unit import utils


class TestActivationStrategy(unittest.TestCase):
    """Tests for the activation strategy."""

    @hypothesis.given(
        activation_layer=hypothesis_torch.same_shape_activation_strategy(),
    )
    def test_activation_strategy(self, activation_layer: torch.nn.Module) -> None:
        """Test that the activation strategy generates an activation layer."""
        batch_size = 3
        input_shape = (batch_size, 5)
        input_tensor = torch.ones(input_shape)
        output_tensor = activation_layer(input_tensor)

        self.assertIsInstance(activation_layer, torch.nn.Module)
        self.assertEqual(output_tensor.shape, input_shape)


class TestLinearStrategy(unittest.TestCase):
    """Tests for the linear strategy."""

    @hypothesis.settings(deadline=None)  # This can be slow.
    @hypothesis.given(
        module_and_kwargs=utils.meta_strategy_constraints(
            strategy_func=hypothesis_torch.linear_network_strategy,
            input_shape=st.integers(min_value=1, max_value=5).map(lambda x: [x]),
            output_shape=st.integers(min_value=1, max_value=5).map(lambda x: [x]),
            device=hypothesis_torch.device_strategy(),
            activation_layer=hypothesis_torch.same_shape_activation_strategy(),
            num_hidden_layers=st.integers(min_value=0, max_value=3),
            hidden_layer_size=st.integers(min_value=1, max_value=5),
        ),
    )
    def test_linear_strategy(self, module_and_kwargs: tuple[torch.nn.Sequential, dict[str, Any]]) -> None:
        """Test that the linear strategy generates a linear network."""
        module, kwargs = module_and_kwargs
        batch_size = 3
        input_shape = (batch_size, *kwargs["input_shape"])
        output_shape = (batch_size, *kwargs["output_shape"])

        input_tensor = torch.ones(input_shape, device=kwargs["device"])
        output_tensor = module(input_tensor)

        self.assertIsInstance(module, torch.nn.Module)

        self.assertEqual(output_tensor.shape, torch.Size(output_shape))
        self.assertEqual(len(module), kwargs["num_hidden_layers"] * 2 + 2)
        for i, layer in enumerate(module):
            if i % 2 == 0:
                self.assertIsInstance(layer, torch.nn.Linear)
                if i == 0:
                    self.assertEqual(layer.weight.shape[1], kwargs["input_shape"][-1])
                elif i == len(module) - 1:
                    self.assertEqual(layer.weight.shape[0], kwargs["output_shape"][-1])
                else:
                    self.assertEqual(layer.weight.shape[1], kwargs["hidden_layer_size"])
            else:
                self.assertIsInstance(layer, torch.nn.Module)
                self.assertIsInstance(layer, type(kwargs["activation_layer"]))

        # Torch devices are not directly comparable. We can compare the device type and index.
        # Device index 0 is considered the same as index `None`.
        self.assertEqual(output_tensor.device.type, kwargs["device"].type)
        if output_tensor.device.index in (0, None):
            assert kwargs["device"].index in (0, None)
        else:
            self.assertEqual(output_tensor.device.index, kwargs["device"].index)
