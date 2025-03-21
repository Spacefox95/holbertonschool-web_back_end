#!/usr/bin/env python3
""" BasicCache defines:
- put to assign key/value in cache_data
- get to get the value of a key"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache is a caching system"""

    def put(self, key, item):
        """Assign the item value for the key to the dict self.cache_data"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to key in the cache data."""
        if key not in self.cache_data or key is None:
            return None
        return self.cache_data.get(key)
