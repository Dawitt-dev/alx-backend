#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ MRUCache defines a MRU caching system.
    """

    def __init__(self):
        """ Initialize the cache system.
        """
        super().__init__()
        self.cache_data = OrderedDict()  # OrderedDict to track order of usage

    def put(self, key, item):
        """ Add an item in the cache.

        Args:
            key (str): The key for the item.
            item (str): The value to be stored.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key.

        Args:
            key (str): The key for the item.

        Returns:
            str: The value associated with the key,
            or None if the key does not exist.
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)  # Mark the key as recently used
        return self.cache_data[key]
