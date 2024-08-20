#!/usr/bin/env python3
"""FIFOCache module"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    FIFOCache defines a FIFO caching system.
    This class inherits from BaseCaching and implements put and get methods.
    """

    def __init__(self):
        """
        Initialize the FIFOCache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Assign the item value to the dictionary self.cache_data for the key.
        If key or item is None, this method does nothing.
        If the number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS, discard the first item put in cache (FIFO).

        Args:
            key: The key to store the item under.
            item: The item to store.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key not in self.cache_data:
                    discarded_key, _ = self.cache_data.popitem(last=False)
                    print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

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
