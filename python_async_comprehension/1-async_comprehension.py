#!/usr/bin/env python3
"""
Using async comprehensing, return 10 random number
"""

import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """ Retuns 10 random numbers"""
    result = []
    async for i in async_generator():
        result.append(i)
    return result
