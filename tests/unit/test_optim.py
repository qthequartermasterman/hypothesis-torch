"""Tests for the `hypothesis_torch.optim` module."""

import unittest

import hypothesis_torch
import hypothesis
from hypothesis import strategies as st

import torch


class TestOptimizerTypeStrategy(unittest.TestCase):
    """Tests for the `optimizer_type_strategy` function."""

    @hypothesis.given(optimizer_type=hypothesis_torch.optimizer_type_strategy())
    def test_optimizer_type_strategy(self, optimizer_type: type[torch.optim.Optimizer]) -> None:
        """Test that `optimizer_type_strategy` generates valid optimizer types."""
        self.assertTrue(issubclass(optimizer_type, torch.optim.Optimizer))
        self.assertNotEqual(optimizer_type, torch.optim.Optimizer)
        self.assertNotIn("NewCls", optimizer_type.__name__)

    @hypothesis.given(
        optimizer_type=hypothesis_torch.optimizer_type_strategy(allowed_optimizer_types=[torch.optim.Adam])
    )
    def test_optimizer_type_strategy_allowed_optimizer_types(self, optimizer_type: type[torch.optim.Optimizer]) -> None:
        """Test that `optimizer_type_strategy` generates optimizer types when specifying `allowed_optimizer_types`."""
        self.assertEqual(optimizer_type, torch.optim.Adam)


class TestOptimizerStrategy(unittest.TestCase):
    """Tests for the `optimizer_strategy` function."""

    @hypothesis.settings(deadline=None)
    @hypothesis.given(
        optimizer_constructor=hypothesis_torch.optimizer_strategy(),
        module=hypothesis_torch.linear_network_strategy(
            input_shape=(1, 1),
            output_shape=(1, 1),
            activation_layer=torch.nn.ReLU(),
            hidden_layer_size=st.integers(min_value=1, max_value=10),
            num_hidden_layers=st.integers(min_value=1, max_value=10),
            device=hypothesis_torch.device_strategy(),
        ),
    )
    def test_optimizer_strategy(
        self, optimizer_constructor: hypothesis_torch.OptimizerConstructorWithOnlyParameters, module: torch.nn.Module
    ) -> None:
        """Test that `optimizer_strategy` generates valid optimizers."""
        optimizer = optimizer_constructor(module.parameters())
        self.assertIsInstance(optimizer, torch.optim.Optimizer)
