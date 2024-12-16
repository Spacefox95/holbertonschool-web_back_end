#!/usr/bin/python3
""" FIFOCache
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache implements a FIFO caching system"""

    def __init__(self):
        """ Initialize the cache and order tracker"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item to the cache with FIFO eviction if needed"""
        if key is not None or item is not None:
            if key not in self.cache_data:
                self.order.append(key)
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print(f'DISCARD: {oldest_key}')

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
