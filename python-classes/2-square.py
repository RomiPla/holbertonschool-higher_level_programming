#!/usr/bin/python3
"""
	Defining an object class named Square
"""


class Square:
    """
        Creating the attribute for sai object
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size