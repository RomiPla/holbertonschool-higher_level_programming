#!/usr/bin/python3
"""
    Modulo
"""

Rectangle = __import__('9-rectangle').Rectangle
"""
    Class Rectangle
"""


class Square(Rectangle):
    """
        Class Square
    """
    def __init__(self, size):
        """
            init
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
