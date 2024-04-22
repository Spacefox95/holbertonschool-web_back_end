#!/usr/bin/env python3
"""
Async fct listing all the delays
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ List all the delays """
    delay: List[float] = []
    index = [wait_random(max_delay) for _ in range(n)]
    for i in asyncio.as_completed(index):
        new_delay = await i
        delay.append(new_delay)
    return delay
