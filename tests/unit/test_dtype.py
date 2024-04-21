import unittest

import hypothesis
import torch

import hypothesis_torch.dtype


class TestDtype(unittest.TestCase):
    @hypothesis.given(dtype=...)
    def test_dtype_strategy(self, dtype: torch.dtype):
        """Test that using the registered `torch.dtype` strategy gives a dtype."""
        self.assertIsInstance(dtype, torch.dtype)
        self.assertIn(dtype, hypothesis_torch.dtype.ALL_DTYPES)

    @hypothesis.given(dtype=hypothesis_torch.dtype.dtype_strategy(elements=hypothesis_torch.dtype.INT_DTYPES))
    def test_dtype_strategy_int(self, dtype: torch.dtype):
        """Test that the dtype strategy when specifying a list of dtypes only generates dtypes in that list."""
        self.assertIsInstance(dtype, torch.dtype)
        self.assertIn(dtype, hypothesis_torch.dtype.INT_DTYPES)

    @hypothesis.given(dtype=hypothesis_torch.dtype.dtype_strategy(elements=hypothesis_torch.dtype.FLOAT_DTYPES))
    def test_dtype_strategy_float(self, dtype: torch.dtype):
        """Test that the dtype strategy when specifying a list of dtypes only generates dtypes in that list."""
        self.assertIsInstance(dtype, torch.dtype)
        self.assertIn(dtype, hypothesis_torch.dtype.FLOAT_DTYPES)

    @hypothesis.given(dtype=hypothesis_torch.dtype.dtype_strategy())
    def test_dtype_strategy_default(self, dtype: torch.dtype):
        """Test that the default arguments of dtype strategy can generate any dtype."""
        self.assertIsInstance(dtype, torch.dtype)
        self.assertIn(dtype, hypothesis_torch.dtype.ALL_DTYPES)
