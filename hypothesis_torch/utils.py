from __future__ import annotations

import itertools
import sys
from typing import Iterable, TypeVar, Tuple, Generator

T = TypeVar("T")

if sys.version_info < (3, 10):

    def pairwise(iterable: Iterable[T]) -> Iterable[Tuple[T, T]]:
        # pairwise('ABCDEFG') --> AB BC CD DE EF FG
        a, b = itertools.tee(iterable)
        next(b, None)
        return zip(a, b)
else:
    pass


def alternate(iterable1: Iterable[T], iterable2: Iterable[T]) -> Generator[T, None, None]:
    fillvalue = object()
    it1 = iter(iterable1)
    it2 = iter(iterable2)
    for pair in itertools.zip_longest(it1, it2, fillvalue=fillvalue):
        for element in pair:
            if element is not fillvalue:
                yield element
