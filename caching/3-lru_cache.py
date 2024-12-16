#!/usr/bin/python3
""" LRUCache
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache implements a LRU caching system"""

    def __init__(self):
        """ Initialize the cache and order tracker"""
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """Add an item to the cache with LRU eviction if needed"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.access_order.remove(key)
            self.cache_data[key] = item
            self.access_order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lru_key = self.access_order.pop(0)
                print(f'DISCARD: {lru_key}')
                del self.cache_data[lru_key]

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        self.access_order.remove(key)
        self.access_order.append(key)
        return self.cache_data[key]
