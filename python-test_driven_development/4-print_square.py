#!/usr/bin/python3
"""
    Se utiliza la misma función que en el proyecto anterior
"""


def print_square(size):
    """
       rgregergerg
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    elif size < 0:
        raise ValueError("size must be >= 0")

    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for a in range(size):
        print("#" * size)
