"""Test the memory_format strategies."""

import unittest

import hypothesis
import torch
import hypothesis_torch

LIMITED_MEMORY_FORMATS = [torch.contiguous_format, torch.channels_last]


class TestMemoryFormat(unittest.TestCase):
    """Tests for the memory_format strategies."""

    @hypothesis.given(memory_format=...)
    def test_inferred_memory_format_strategy(self, memory_format: torch.memory_format) -> None:
        """Test that the inferred memory_format strategy generates a memory_format."""
        self.assertIsInstance(memory_format, torch.memory_format)

    @hypothesis.given(
        memory_format=hypothesis_torch.memory_format_strategy(),
    )
    def test_default_memory_format_strategy(self, memory_format: torch.memory_format) -> None:
        """Test that the default memory_format strategy generates a memory_format."""
        self.assertIsInstance(memory_format, torch.memory_format)

    @hypothesis.given(memory_format=hypothesis_torch.memory_format_strategy(LIMITED_MEMORY_FORMATS))
    def test_limited_memory_format_strategy(self, memory_format: torch.memory_format) -> None:
        """Test that the limited memory_format strategy generates a memory_format."""
        self.assertIsInstance(memory_format, torch.memory_format)
        self.assertIn(memory_format, LIMITED_MEMORY_FORMATS)
