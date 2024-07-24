#!/usr/bin/env python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines a simple cache system without a limit.
    """

    def put(self, key, item):
        """ Add an item in the cache.

        Args:
            key (str): The key for the item.
            item (str): The value to be stored.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key.

        Args:
            key (str): The key for the item.

        Returns:
            str: The value associated with the key,
            or None if the key does not exist.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
