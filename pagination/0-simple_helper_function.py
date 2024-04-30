#!/usr/bin/env python3
"""
Function that return a tuple of size two
containing a start and an end index
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Function corresponding to the range of indexes
    """
    start_index = (page - 1) * page_size
    end_index = (page * page_size)
    if end_index > page_size:
        end_index == page_size
    return (start_index, end_index)
