"""Utility iterable functions."""

from __future__ import annotations

import itertools
import sys
from collections.abc import Generator, Iterable
from typing import TypeVar, cast

T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)

if sys.version_info < (3, 10):  # pragma: no cover

    def pairwise(iterable: Iterable[T]) -> Iterable[tuple[T, T]]:  # pragma: no cover
        """Iterate over pairs of consecutive elements in an iterable.

        Note:
            This is a backport of the `pairwise` function from Python 3.10 (for older versions of Python).

        Args:
            iterable: The iterable to iterate over.

        Returns:
            An iterable of pairs of consecutive elements.

        """
        # pairwise('ABCDEFG') --> AB BC CD DE EF FG
        a, b = itertools.tee(iterable)
        next(b, None)
        return zip(a, b)

else:  # pragma: no cover
    pairwise = itertools.pairwise


def alternate(iterable1: Iterable[T_co], iterable2: Iterable[T_co]) -> Generator[T_co, None, None]:
    """Alternate elements from two iterables.

    Args:
        iterable1: The first iterable.
        iterable2: The second iterable.

    Yields:
        Elements from the two iterables in alternation.

    """
    fill_value = object()
    it1 = iter(iterable1)
    it2 = iter(iterable2)
    for pair in itertools.zip_longest(it1, it2, fillvalue=fill_value):
        for element in pair:
            if element is not fill_value:
                yield cast(T_co, element)
