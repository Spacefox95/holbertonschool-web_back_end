#!/usr/bin/env python3
"""
Coroutine looping 10times and yield a random number
"""

import asyncio
import random


async def async_generator():
    """ Yield a random number """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
