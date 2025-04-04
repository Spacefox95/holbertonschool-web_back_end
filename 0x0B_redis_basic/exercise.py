#!/usr/bin/env python3

""" Cache class for redis"""

from typing import Union
import uuid
import redis


class Cache():
    """ Base Cache class"""
    def __init__(self) -> None:
        """ Cache class variables"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str | bytes | int | float]) -> str:
        """ Generate a key and store the data in redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
