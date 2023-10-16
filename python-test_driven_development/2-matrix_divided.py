#!/usr/bin/python3
"""
	Este modulo
	divide enteros
"""


def matrix_divided(matrix, div):
    """
    funcion de divicion
    retorna una matriz con los
    valores divididos.
    la matriz es una lista de listas
    cada lista tiene solos int o float.
    las listas no pueden estar vacias y
    el divisor tiene que se mayor que 0
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    l0 = []
    for a in matrix:
        if type(a) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

        if len(a) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have \
the same size")

        l1 = []
        for b in a:
            if type(b) is not int and type(b) is not float:
                raise TypeError("matrix mut be a matrix (list of lists) of \
integers/floats")

            l1.append(round(b / div, 2))
        l0.append(l1)
    return l0
