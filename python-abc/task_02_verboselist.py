#!/usr/bin/env python3
"""
    kefkjknke
"""


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")
    
    def extend(self, iterable):
        items_count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{items_count}] items.")
    
    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)
    
    def pop(self, index=None):
        if index is None:
            item = super().pop()
            print(f"Popped [{item}] from the list.")
            return item
        else:
            item = super().pop(index)
            print(f"Popped [{item}] from the list.")
            return item
