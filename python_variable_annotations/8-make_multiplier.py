#!/usr/bin/env python3
"""
Function multiplying a float
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Multiplies pultiplier by a float"""
    return lambda x: x * multiplier
