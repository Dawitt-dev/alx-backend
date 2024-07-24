#!/usr/bin/python3
"""
a class that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """a a FIFO caching system"""

    def __init__(self):
        """Initialize the cache system"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache."""
        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldkey, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {oldkey}")

        self.cache_data[key] = item

        def get(self, key):
            """ Get an item by key """
            return self.cache_data.get(key, None)
