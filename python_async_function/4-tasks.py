#!/usr/bin/env python3
"""
Create a task as wait_random is working
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random
wait_n = __import__('1-concurrent_coroutines').wait_n


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Function creating a task"""
    delay: List[float] = []
    index = [task_wait_random(max_delay) for _ in range(n)]
    for i in asyncio.as_completed(index):
        new_delay = await i
        delay.append(new_delay)
    return delay
