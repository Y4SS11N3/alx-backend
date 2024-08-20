#!/usr/bin/env python3
"""LFUCache module"""
from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """
    LFUCache defines a Least Frequently Used (LFU) caching system.
    This class inherits from BaseCaching and implements put and get methods.
    """

    def __init__(self):
        """
        Initialize the LFUCache.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_frequency = defaultdict(int)
        self.frequency_list = defaultdict(OrderedDict)
        self.min_frequency = 0

    def put(self, key, item):
        """
        Assign the item value to the dictionary self.cache_data for the key.
        If key or item is None, this method does nothing.
        If the number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS, discard the least frequently
        used item (LFU algorithm).
        If there is more than 1 item with the lowest frequency,
        use LRU algorithm.

        Args:
            key: The key to store the item under.
            item: The item to store.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self._update_frequency(key)
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            self._remove_least_frequent()

        self.cache_data[key] = item
        self.keys_frequency[key] = 1
        self.frequency_list[1][key] = None
        self.min_frequency = 1

    def get(self, key):
        """
        Return the value linked to the given key from self.cache_data.
        If key is None or doesn't exist in self.cache_data, return None.
        Update the frequency of the accessed item.

        Args:
            key: The key to retrieve the item for.

        Returns:
            The value associated with the key, or None if the key is not found.
        """
        if key is None or key not in self.cache_data:
            return None

        self._update_frequency(key)
        return self.cache_data[key]

    def _update_frequency(self, key):
        """
        Update the frequency of the given key.
        Move the key to the next frequency level.

        Args:
            key: The key to update the frequency for.
        """
        freq = self.keys_frequency[key]
        self.keys_frequency[key] += 1
        del self.frequency_list[freq][key]
        if not self.frequency_list[freq]:
            if freq == self.min_frequency:
                self.min_frequency += 1
            del self.frequency_list[freq]
        self.frequency_list[freq + 1][key] = None

    def _remove_least_frequent(self):
        """
        Remove the least frequently used item from the cache.
        If there are multiple items with the same lowest frequency,
        remove the least recently used among them.
        """
        lfu_key = next(iter(self.frequency_list[self.min_frequency]))
        del self.cache_data[lfu_key]
        del self.keys_frequency[lfu_key]
        del self.frequency_list[self.min_frequency][lfu_key]
        if not self.frequency_list[self.min_frequency]:
            del self.frequency_list[self.min_frequency]
        print(f"DISCARD: {lfu_key}")
