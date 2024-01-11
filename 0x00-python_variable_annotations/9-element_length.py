#!/usr/bin/env python3
"""Module containing type-annotated functions"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function that returns a list of tuples containing elements and length"""
    return [(i, len(i)) for i in lst]
