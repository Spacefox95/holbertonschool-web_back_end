#!/usr/bin/python3
""" MRUCache
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache implements a MRU caching system"""

    def __init__(self):
        """ Initialize the cache and order tracker"""
        super().__init__()
        self.most_recent_key = None

    def put(self, key, item):
        """Add an item to the cache with MRU eviction if needed"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    print(f"DISCARD: {self.most_recent_key}")
                    del self.cache_data[self.most_recent_key]
                self.cache_data[key] = item
            self.most_recent_key = key

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        self.most_recent_key = key
        return self.cache_data[key]
