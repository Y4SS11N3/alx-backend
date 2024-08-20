#!/usr/bin/env python3
"""BasicCache module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache defines a basic caching system with no limit.
    This class inherits from BaseCaching and implements put and get methods.
    """

    def put(self, key, item):
        """
        Assign the item value to the dictionary self.cache_data for the key.
        If key or item is None, this method does nothing.

        Args:
            key: The key to store the item under.
            item: The item to store.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

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
