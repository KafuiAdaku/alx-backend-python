#!/usr/bin/env python3
"""Module containing type-annotated functions"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Function that returns the first element of a list"""
    if lst:
        return lst[0]
    else:
        return None
