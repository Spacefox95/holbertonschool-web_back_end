#!/usr/bin/python3
""" LIFOCache
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache implements a LIFO caching system"""

    def __init__(self):
        """ Initialize the cache and order tracker"""
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Add an item to the cache with LIFO eviction if needed"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if self.last_key is not None:
                    print(f'DISCARD: {self.last_key}')
                    del self.cache_data[self.last_key]
            self.last_key = key

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
