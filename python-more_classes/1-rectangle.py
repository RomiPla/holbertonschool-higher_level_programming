#!/usr/bin/python3
"""
    Define un clase de objeto llamado Square
"""


class Rectangle:
    """
        Creando el atributo para el objeto
    """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

    @property
    def height(self):
        """Establecer propiedades para square"""
        return self.__height

    @height.setter
    def height(self, value):
        """Definir cualificaciones de Height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Establecer propiedades para square"""
        return self.__width

    @width.setter
    def width(self, value):
        """Definir cialificaciones para Size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
