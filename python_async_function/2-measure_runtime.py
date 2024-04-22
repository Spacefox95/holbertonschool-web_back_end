#!/usr/bin/env python3
"""
Measure total execution tome
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Return the total execution time """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    result: float = (end_time - start_time) / n
    return result
