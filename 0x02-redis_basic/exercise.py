#!/usr/bin/env python3
""" This module for implementing redis basics. """

import redis
from typing import Union, Callable, Optional
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """ Count how many times methods of the Cache class are called """
    key = method.__qualname__

class Cache:
    """ Redis cache storage. """
    def __init__(self):
        """ For initializing redis object. """
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ akes a data argument and returns a string. It generate a
            random key (e.g. using uuid), store the input data in Redis
            using the random key and return the key.
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float]:
        """ Take a key string argument and an optional Callable argument fn.
            This fn will convert the data back to the desired format.
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)

        return value

    def get_str(self, key: str) -> str:
        """ Automatically parametrize Cache.get with the correct format """
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """ Automatically parametrize Cache.get with the correct format """
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
