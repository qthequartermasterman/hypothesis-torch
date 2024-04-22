import unittest
import hypothesis
from hypothesis import strategies as st
from hypothesis_torch import utils

class TestPairwise(unittest.TestCase):
    @hypothesis.given(iterable=st.lists(st.integers()))
    def test_pairwise(self, iterable:list[int]):
        """Test that the pairwise strategy generates pairs of integers."""
        pairs = list(utils.pairwise(iterable))
        if len(iterable) == 0 or len(iterable) == 1:
            self.assertEqual(pairs, [])
            return

        self.assertEqual(len(pairs), len(iterable)-1)
        for i, pair in enumerate(pairs):
            self.assertIsInstance(pair, tuple)
            self.assertEqual(len(pair), 2)
            self.assertIsInstance(pair[0], int)
            self.assertIsInstance(pair[1], int)
            self.assertEqual(pair[0], iterable[i])
            self.assertEqual(pair[1], iterable[i+1])

class TestAlternate(unittest.TestCase):
    @hypothesis.given(iterable1=st.lists(st.integers()),
                      iterable2=st.lists(st.integers()))
    def test_alternate(self, iterable1:list[int],iterable2:list[int]):
        """Test that the alternate strategy generates alternating integers."""
        alternates = list(utils.alternate(iterable1, iterable2))
        self.assertEqual(len(alternates), len(iterable1) + len(iterable2))
        if len(iterable1) == 0:
            self.assertEqual(alternates, iterable2)
            return
        if len(iterable2) == 0:
            self.assertEqual(alternates, iterable1)
            return

        shorter_iterable_length = min(len(iterable1), len(iterable2))

        for i, alternate in enumerate(alternates):
            # There are two chunks
            # the first chunk is the part where it alternates between the first and second iterable
            # the second chunk is the part where it yields the rest of the longer iterable
            if i < 2*shorter_iterable_length:
                if i % 2 == 0:
                    self.assertIsInstance(alternate, int)
                    self.assertEqual(alternate, iterable1[i//2])
                else:
                    self.assertIsInstance(alternate, int)
                    self.assertEqual(alternate, iterable2[i//2])
            else:
                if len(iterable1) > len(iterable2):
                    self.assertEqual(alternate, iterable1[i - shorter_iterable_length])
                else:
                    self.assertEqual(alternate, iterable2[i - shorter_iterable_length])
