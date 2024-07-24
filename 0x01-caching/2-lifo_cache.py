#!/usr/bin/env python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines a LIFO caching system.
    """

    def __init__(self):
        """ Initialize the cache system.
        """
        super().__init__()
        self.order = []  # List to keep track of the order of keys (LIFO)

    def put(self, key, item):
        """ Add an item in the cache.

        Args:
            key (str): The key for the item.
            item (str): The value to be stored.
        """
        if key is None or item is None:
            return

        # If the key already exists, remove it from the order list
        if key in self.cache_data:
            self.order.remove(key)
        else:
            # If cache exceeds max items, discard the last item (LIFO)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = self.order.pop()  # Get the last item added (LIFO)
                del self.cache_data[last_key]  # Remove the last item
                print(f"DISCARD: {last_key}")

        # Add the new item to the cache and update the order
        self.cache_data[key] = item
        self.order.append(key)

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
