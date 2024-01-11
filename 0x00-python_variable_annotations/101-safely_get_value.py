#!/usr/bin/env python3
"""Module containing type-annotated fucntions"""
from typing import Any, Mapping, TypeVar, Union


T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None] = None) -> Union[Any, T]:
    """Function that returns the value of a key safely"""
    if key in dct:
        return dct[key]
    else:
        return default
