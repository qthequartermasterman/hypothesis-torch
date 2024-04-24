"""Tests for registering the random torch state."""

import unittest

import hypothesis.internal.entropy

import hypothesis_torch
import torch


class TestRegisterRandomTorchState(unittest.TestCase):
    """Tests for registering the random torch state."""

    def test_register_random_torch_state(self) -> None:
        """Test that the torch random state is registered."""
        self.assertIn(hypothesis_torch.TORCH_RANDOM_WRAPPER, hypothesis.internal.entropy.RANDOMS_TO_MANAGE.values())
