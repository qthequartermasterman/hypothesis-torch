"""Tests for the tensor strategy."""

import unittest
from typing import Any

import hypothesis
import torch
from hypothesis import strategies as st

import hypothesis_torch
from tests.unit import utils


class TestTensor(unittest.TestCase):
    """Tests for the tensor strategy."""

    # TODO: Figure out a way to test passing in strategies into the arguments of the tensor_strategy.

    @hypothesis.given(tensor=...)
    def test_tensor_strategy_registered(self, tensor: torch.Tensor) -> None:
        """Test that the registered tensor strategy generates tensors."""
        self.assertIsInstance(tensor, torch.Tensor)

    @hypothesis.given(
        tensor_and_kwargs=utils.meta_strategy_constraints(
            strategy_func=hypothesis_torch.tensor.tensor_strategy,
            dtype=hypothesis_torch.dtype_strategy(),
            shape=st.lists(st.integers(min_value=1, max_value=10), min_size=1, max_size=3),
            device=hypothesis_torch.device_strategy(),
        ),
    )
    def test_tensor_strategy_fixed_arguments(self, tensor_and_kwargs: tuple[torch.Tensor, dict[str, Any]]) -> None:
        """Test that the registered tensor strategy generates tensors."""
        tensor, kwargs = tensor_and_kwargs
        self.assertIsInstance(tensor, torch.Tensor)
        self.assertEqual(tensor.dtype, kwargs["dtype"])
        self.assertEqual(tensor.shape, torch.Size(kwargs["shape"]))

        # Device equality is not directly comparable. We can compare the device type and index.
        # Device index 0 is considered the same as index `None`.
        self.assertEqual(tensor.device.type, kwargs["device"].type)
        if tensor.device.index in (0, None):
            assert kwargs["device"].index in (0, None)
        else:
            self.assertEqual(tensor.device.index, kwargs["device"].index)
