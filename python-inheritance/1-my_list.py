#!/usr/bin/python3
"""
    Modulo que imprime sorted list
"""


class MyList(list):
    """
        Class named MyList
    """

    def print_sorted(self):
        """
            Prints the list but sorted (ascending sort)
        """
        print(sorted(self))
