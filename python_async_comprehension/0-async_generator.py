#!/usr/bin/env python3
"""
Coroutine looping 10times and yield a random number
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Yield a random number """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
