"""Test the layout strategies."""

import unittest

import hypothesis
import torch
import hypothesis_torch

LIMITED_LAYOUTS = [torch.strided]


class TestLayout(unittest.TestCase):
    """Tests for the layout strategies."""

    @hypothesis.given(layout=...)
    def test_inferred_layout_strategy(self, layout: torch.layout) -> None:
        """Test that the inferred layout strategy generates a layout."""
        self.assertIsInstance(layout, torch.layout)

    @hypothesis.given(
        layout=hypothesis_torch.layout_strategy(),
    )
    def test_default_layout_strategy(self, layout: torch.layout) -> None:
        """Test that the default layout strategy generates a layout."""
        self.assertIsInstance(layout, torch.layout)

    @hypothesis.given(layout=hypothesis_torch.layout_strategy(LIMITED_LAYOUTS))
    def test_limited_layout_strategy(self, layout: torch.layout) -> None:
        """Test that the limited layout strategy generates a layout."""
        self.assertIsInstance(layout, torch.layout)
        self.assertIn(layout, LIMITED_LAYOUTS)
