#!/usr/bin/env python3

""" Cache class for redis"""

from typing import Callable, Optional, Union
import uuid
import redis


class Cache():
    """ Base Cache class"""

    def __init__(self):
        """ Cache class variables"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generate a key and store the data in redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[
                str,
                bytes,
                int,
                float, None]:
        """ Get the value"""
        if key:
            value = self._redis.get(key)
            if fn:
                return fn(value)
            return value
        return None

    def get_str(self, key: str) -> Optional[str]:
        """ Get the value for a str key"""
        return self.get(key=key, fn=lambda b: b.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """ Get the value for an int key"""
        return self.get(key=key, fn=int)
