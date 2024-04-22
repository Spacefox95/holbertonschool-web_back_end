#!/usr/bin/env python3
"""
Annotate a function return values
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Return the length of an element"""
    return [(i, len(i)) for i in lst]
