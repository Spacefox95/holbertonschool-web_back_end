#!/usr/bin/env python3
"""
Create a task as wait_random is working
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """ Function creating a task"""
    loop = asyncio.get_event_loop()
    task: asyncio.task = loop.create_task(wait_random(max_delay))
    return task
