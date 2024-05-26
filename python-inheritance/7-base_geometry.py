#!/usr/bin/python3
"""
   Módulo: area(self), integer_validator(self, name, value)
"""


class BaseGeometry:
    """
        Class BaseGeometry
    """
    def area(self):
        """
            Función area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Nombre explicativo"""
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
