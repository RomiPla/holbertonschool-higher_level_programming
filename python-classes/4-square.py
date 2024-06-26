#!/usr/bin/python3
"""
    Definir el objeto
"""


class Square:
    """
        Crear el atributo
    """
 
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Property setter for square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Defining size cualifications"""
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size
