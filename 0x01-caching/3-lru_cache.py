#!/usr/bin/env python3
""" LRUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRUCache defines a LRU caching system.
    """

    def __init__(self):
        """ Initialize the cache system.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache.

        Args:
            key (str): The key for the item.
            item (str): The value to be stored.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {lru_key}")

        # Add the new item to the cache and mark it as recently used
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key.

        Args:
            key (str): The key for the item.

        Returns:
            str: The value associated with the key, or
            None if the key does not exist.
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)  # Mark the key as recently used
        return self.cache_data[key]
