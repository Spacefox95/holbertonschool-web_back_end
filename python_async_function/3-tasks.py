#!/usr/bin/env python3
"""
Create a task as wait_random is working
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """ Function creating a task"""
    task: asyncio.task = asyncio.create_task(wait_random(max_delay))
    return task
