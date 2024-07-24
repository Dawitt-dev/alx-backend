#!/usr/bin/python3
"""
a class that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching
from collections import deque


class FIFOCache(BaseCaching):
    """a a FIFO caching system"""

    def __init__(self):
        """Initialize the cache system"""
        super().__init__()
        self.order = deque()

    def put(self, key, item):
        """Add an item in the cache."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key = self.order.popleft()
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

        self.cache_data[key] = item
        self.order.append(key)

        def get(self, key):
            """ Get an item by key """
            if key is None:
                return None
            return self.cache_data.get(key)
