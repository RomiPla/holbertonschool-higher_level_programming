#!/usr/bin/python3
"""
	Este modulo
	suma enteros
"""


def add_integer(a, b=98):
    """
    funcion de suma de enteros con 2 argumentos,
    esta funcion retorna la suma de a y b.
    a - es un entero y es el primer sumando
    b - es un entero y es el segundo sumando
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    a = int(a)
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    b = int(b)

    return a + b
