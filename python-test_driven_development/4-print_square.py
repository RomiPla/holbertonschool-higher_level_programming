#!/usr/bin/python3
"""
	Modulo Print Square
	imprime un cuadrado usando #
	Los argumentos que recibe la
	funcion dterminan el ancho y largo
	de la figura
"""


def print_square(size):
    """
    imprime un cuadrado
    siempre que los ags
    sean int o float
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    elif size < 0:
        raise ValueError("size must be >= 0")

    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for a in range(size):
        print("#" * size)
