import unittest
import hypothesis.strategies as st
import hypothesis
import torch


class TestTensor(unittest.TestCase):
    @hypothesis.given(tensor=...)
    def test_tensor_strategy(self, tensor: torch.Tensor) -> None:
        """Test that the registered tensor strategy generates tensors."""
        self.assertIsInstance(tensor, torch.Tensor)
