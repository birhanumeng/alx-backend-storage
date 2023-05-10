#!/usr/bin/env python3
""" This module for implementing redis basics. """

import redis
from typing import Union
from uuid import uuid4


class Cache:
    """ Redis cache storage. """
    def __init__(self):
        """ For initializing redis object. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ akes a data argument and returns a string. It generate a
            random key (e.g. using uuid), store the input data in Redis
            using the random key and return the key.
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
