#!/usr/bin/env python3

""" Cache class for redis"""

from functools import wraps
from typing import Callable, Optional, Union
import uuid
import redis


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):

        input_key = method.__qualname__ + ":inputs"
        ouput_key = method.__qualname__ + ":outputs"

        self._redis.rpush(input_key, str(args))

        result = method(self, *args, **kwargs)
        self._redis.rpush(ouput_key, str(result))

        return result
    return wrapper


class Cache():
    """ Base Cache class"""

    def __init__(self):
        """ Cache class variables"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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

    def replay(method: Callable):
        replay = method._self._redis
        qualname = method.__qualname__

        input_key = method.__qualname__ + ":inputs"
        ouput_key = method.__qualname__ + ":outputs"

        inputs = replay.lrange(input_key, 0, -1)
        outputs = replay.lrange(ouput_key, 0, -1)
        call_count = replay.get(qualname)

        print(f"{qualname} was called {int(call_count)} times:")
        for inp, out in zip(inputs, outputs):
            print(
                f"{qualname}(*{inp.decode('utf-8')}) -> {out.decode('utf-8')}")
