#!/usr/bin/python3
"""
    Define un clase de objeto llamado Square
"""


class Rectangle:
    """
        Creando el atributo para el objeto
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width
        type(self).number_of_instances += 1

    print_symbol = "#"

    @property
    def height(self):
        """Establecer propiedades para square"""
        return self.__height

    @height.setter
    def height(self, value):
        """Definir cualificaciones de Height"""
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
            saved_str += str(f"{self.print_symbol}" * self.__width) + '\n'
        saved_str = saved_str[:-1]
        return saved_str

    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            elif rect_2.area() > rect_1.area():
                return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
        