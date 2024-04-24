"""Tests for the tensor strategy."""

import unittest
from typing import Any

import hypothesis
import torch
from hypothesis import strategies as st

import hypothesis_torch
from tests.unit import utils

INT8_RANGE = {
    "min_value": -128,
    "max_value": 127,
}

INT16_RANGE = {
    "min_value": -32768,
    "max_value": 32767,
}

INT32_RANGE = {
    "min_value": -2147483648,
    "max_value": 2147483647,
}

INT64_RANGE = {
    "min_value": -9223372036854775808,
    "max_value": 9223372036854775807,
}

UINT8_RANGE = {
    "min_value": 0,
    "max_value": 255,
}


class TestTensor(unittest.TestCase):
    """Tests for the tensor strategy."""

    # TODO: Figure out a way to test passing in strategies into the arguments of the tensor_strategy.

    @hypothesis.given(tensor=...)
    def test_tensor_strategy_registered(self, tensor: torch.Tensor) -> None:
        """Test that the registered tensor strategy generates tensors."""
        self.assertIsInstance(tensor, torch.Tensor)

    @hypothesis.given(
        tensor_and_kwargs=utils.meta_strategy_constraints(
            strategy_func=hypothesis_torch.tensor_strategy,
            dtype=hypothesis_torch.dtype_strategy(),
            shape=st.lists(st.integers(min_value=1, max_value=10), min_size=1, max_size=3).map(tuple),
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

    @hypothesis.given(
        tensor=hypothesis_torch.tensor_strategy(
            dtype=torch.float32,
            shape=st.lists(st.integers(min_value=1, max_value=10), min_size=1, max_size=3).map(tuple),
            elements=st.floats(min_value=-10, max_value=10),
        )
    )
    def test_single_precision_tensor_with_double_precision_elements(self, tensor: torch.Tensor) -> None:
        """Test that the giving a single precision dtype and double precision elements successfully coerces the tensor
        to single precision without throwing an error.
        """
        self.assertEqual(tensor.dtype, torch.float32)

    @hypothesis.given(
        tensor=hypothesis_torch.tensor_strategy(
            dtype=torch.float16,
            shape=st.lists(st.integers(min_value=1, max_value=10), min_size=1, max_size=3).map(tuple),
            elements=st.floats(min_value=-10, max_value=10),
        )
    )
    def test_half_precision_tensor_with_double_precision_elements(self, tensor: torch.Tensor) -> None:
        """Test that the giving a half precision dtype and double precision elements successfully coerces the tensor
        to half precision without throwing an error.
        """
        self.assertEqual(tensor.dtype, torch.float16)

    @hypothesis.given(
        tensor=hypothesis_torch.tensor_strategy(
            dtype=torch.bfloat16,
            shape=st.lists(st.integers(min_value=1, max_value=10), min_size=1, max_size=3).map(tuple),
            elements=st.floats(min_value=-10, max_value=10),
        )
    )
    def test_bfloat16_tensor_with_double_precision_elements(self, tensor: torch.Tensor) -> None:
        """Test that the giving a bfloat16 dtype and double precision elements successfully coerces the tensor
        to bfloat16 precision without throwing an error.
        """
        self.assertEqual(tensor.dtype, torch.bfloat16)

    @hypothesis.given(
        tensor=hypothesis_torch.tensor_strategy(
            dtype=torch.complex64,
            shape=st.lists(st.integers(min_value=1, max_value=10), min_size=1, max_size=3).map(tuple),
            elements=st.complex_numbers(),
        )
    )
    def test_single_precision_complex_tensor_with_double_precision_elements(self, tensor: torch.Tensor) -> None:
        """Test that the giving a single precision complex dtype and double precision elements successfully coerces
        the tensor to single precision complex without throwing an error.
        """
        self.assertEqual(tensor.dtype, torch.complex64)

    @hypothesis.given(
        tensor=hypothesis_torch.tensor_strategy(
            dtype=torch.int8,
            shape=st.lists(st.integers(min_value=1, max_value=10), min_size=1, max_size=3).map(tuple),
            elements=st.integers(**INT8_RANGE),
        )
    )
    def test_int8_tensor_with_ranged_integer_elements(self, tensor: torch.Tensor) -> None:
        """Test that specifying integer elements within the range of an int8 tensor is of the correct dtype."""
        self.assertEqual(tensor.dtype, torch.int8)

    @hypothesis.given(
        tensor=hypothesis_torch.tensor_strategy(
            dtype=torch.int8,
            shape=st.lists(st.integers(min_value=1, max_value=10), min_size=1, max_size=3).map(tuple),
            elements=st.integers(),
        )
    )
    def test_int8_tensor_with_unranged_integer_elements(self, tensor: torch.Tensor) -> None:
        """Test that specifying integer elements without a range of an int16 tensor is of the correct dtype."""
        self.assertEqual(tensor.dtype, torch.int8)

    @hypothesis.given(
        tensor=hypothesis_torch.tensor_strategy(
            dtype=torch.int16,
            shape=st.lists(st.integers(min_value=1, max_value=10), min_size=1, max_size=3).map(tuple),
            elements=st.integers(**INT16_RANGE),
        )
    )
    def test_int16_tensor_with_ranged_integer_elements(self, tensor: torch.Tensor) -> None:
        """Test that specifying integer elements within the range of an int16 tensor is of the correct dtype."""
        self.assertEqual(tensor.dtype, torch.int16)

    @hypothesis.given(
        tensor=hypothesis_torch.tensor_strategy(
            dtype=torch.int16,
            shape=st.lists(st.integers(min_value=1, max_value=10), min_size=1, max_size=3).map(tuple),
            elements=st.integers(),
        )
    )
    def test_int16_tensor_with_unranged_integer_elements(self, tensor: torch.Tensor) -> None:
        """Test that specifying integer elements without a range of an int32 tensor is of the correct dtype."""
        self.assertEqual(tensor.dtype, torch.int16)

    @hypothesis.given(
        tensor=hypothesis_torch.tensor_strategy(
            dtype=torch.int32,
            shape=st.lists(st.integers(min_value=1, max_value=10), min_size=1, max_size=3).map(tuple),
            elements=st.integers(**INT32_RANGE),
        )
    )
    def test_int32_tensor_with_ranged_integer_elements(self, tensor: torch.Tensor) -> None:
        """Test that specifying integer elements within the range of an int32 tensor is of the correct dtype."""
        self.assertEqual(tensor.dtype, torch.int32)

    @hypothesis.given(
        tensor=hypothesis_torch.tensor_strategy(
            dtype=torch.int32,
            shape=st.lists(st.integers(min_value=1, max_value=10), min_size=1, max_size=3).map(tuple),
            elements=st.integers(),
        )
    )
    def test_int32_tensor_with_unranged_integer_elements(self, tensor: torch.Tensor) -> None:
        """Test that specifying integer elements without a range of an int32 tensor is of the correct dtype."""
        self.assertEqual(tensor.dtype, torch.int32)

    @hypothesis.given(
        tensor=hypothesis_torch.tensor_strategy(
            dtype=torch.int64,
            shape=st.lists(st.integers(min_value=1, max_value=10), min_size=1, max_size=3).map(tuple),
            elements=st.integers(**INT64_RANGE),
        )
    )
    def test_int64_tensor_with_ranged_integer_elements(self, tensor: torch.Tensor) -> None:
        """Test that specifying integer elements within the range of an int64 tensor is of the correct dtype."""
        self.assertEqual(tensor.dtype, torch.int64)

    @hypothesis.given(
        tensor=hypothesis_torch.tensor_strategy(
            dtype=torch.int64,
            shape=st.lists(st.integers(min_value=1, max_value=10), min_size=1, max_size=3).map(tuple),
            elements=st.integers(),
        )
    )
    def test_int64_tensor_with_unranged_integer_elements(self, tensor: torch.Tensor) -> None:
        """Test that specifying integer elements without a range of an int64 tensor is of the correct dtype."""
        self.assertEqual(tensor.dtype, torch.int64)

    @hypothesis.given(
        tensor=hypothesis_torch.tensor_strategy(
            dtype=torch.uint8,
            shape=st.lists(st.integers(min_value=1, max_value=10), min_size=1, max_size=3).map(tuple),
            elements=st.integers(**UINT8_RANGE),
        )
    )
    def test_uint8_tensor_with_ranged_integer_elements(self, tensor: torch.Tensor) -> None:
        """Test that specifying integer elements within the range of an uint8 tensor is of the correct dtype."""
        self.assertEqual(tensor.dtype, torch.uint8)

    @hypothesis.given(
        tensor=hypothesis_torch.tensor_strategy(
            dtype=torch.uint8,
            shape=st.lists(st.integers(min_value=1, max_value=10), min_size=1, max_size=3).map(tuple),
            elements=st.integers(),
        )
    )
    def test_uint8_tensor_with_unranged_integer_elements(self, tensor: torch.Tensor) -> None:
        """Test that specifying integer elements without a range of an uint8 tensor is of the correct dtype."""
        self.assertEqual(tensor.dtype, torch.uint8)

    @hypothesis.given(
        tensor_and_kwargs=utils.meta_strategy_constraints(
            strategy_func=hypothesis_torch.tensor_strategy,
            dtype=hypothesis_torch.dtype_strategy(dtypes=hypothesis_torch.INT_DTYPES),
            shape=st.lists(st.integers(min_value=1, max_value=10), min_size=1, max_size=3).map(tuple),
        )
    )
    def test_int_tensor_is_filled_appropriately_if_no_elements_specified(
        self, tensor_and_kwargs: tuple[torch.Tensor, dict[str, Any]]
    ) -> None:
        """Test that if no elements are specified, the tensor is filled with integers."""
        tensor, kwargs = tensor_and_kwargs
        self.assertEqual(tensor.dtype, kwargs["dtype"])

    @hypothesis.given(
        tensor=hypothesis_torch.tensor_strategy(
            dtype=hypothesis_torch.dtype_strategy(),
            shape=tuple(),
        )
    )
    def empty_tuple_shape_yields_scalar_tensor(self, tensor: torch.Tensor) -> None:
        """Test that an empty tuple shape yields a scalar tensor."""
        self.assertEqual(tensor.shape, torch.Size([]))
