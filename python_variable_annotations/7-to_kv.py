#!/usr/bin/env python3
"""
Function that does a lot of things
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple of diffrent types"""
    return (k, float(v**2))
