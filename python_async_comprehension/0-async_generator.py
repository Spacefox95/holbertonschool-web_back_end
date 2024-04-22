#!/usr/bin/env python3
"""
Coroutine looping 10times and yield a random number
"""

import asyncio
import random


async def async_generator():
    """ Yield a random number """
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 10.0
    while True:
        delay: float = random.uniform(0, 10)
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)
        yield delay
