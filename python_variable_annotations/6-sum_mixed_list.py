#!/usr/bin/env python3
"""
Function returns a list of mixed args
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Sum of a list of floats"""
    return float(sum(mxd_lst))
