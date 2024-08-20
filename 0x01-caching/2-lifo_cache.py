#!/usr/bin/env python3
"""LIFOCache module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache defines a LIFO caching system.
    This class inherits from BaseCaching and implements put and get methods.
    """

    def __init__(self):
        """
        Initialize the LIFOCache.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Assign the item value to the dictionary self.cache_data for the key.
        If key or item is None, this method does nothing.
        If the number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS, discard the last item put in cache (LIFO).

        Args:
            key: The key to store the item under.
            item: The item to store.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key not in self.cache_data:
                    discarded_key = self.order.pop()
                    del self.cache_data[discarded_key]
                    print(f"DISCARD: {discarded_key}")
            if key in self.cache_data:
                self.order.remove(key)

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Return the value linked to the given key from self.cache_data.
        If key is None or doesn't exist in self.cache_data, return None.

        Args:
            key: The key to retrieve the item for.

        Returns:
            The value associated with the key, or None if the key is not found.
        """
        return self.cache_data.get(key) if key is not None else None
