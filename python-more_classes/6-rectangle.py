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

    @property
    def height(self):
        """Establecer propiedades para square"""
        return self.__height

    @height.setter
    def height(self, value):
        """Establecer propiedades para height"""
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
        """Definir cualificaciones de Width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Establecer propiedades para square"""
        return self.__height * self.__width

    def perimeter(self):
        """Definición de cualificaciones perimetrales"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__height * 2 + self.__width * 2

    def __str__(self):
        saved_str = ""
        if self.__height == 0 or self.__width == 0:
            return ('')
        for i in range(self.__height):
            saved_str += str("#" * self.__width) + '\n'
        saved_str = saved_str[:-1]
        return saved_str

    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        print("Bye rectangle...")
        