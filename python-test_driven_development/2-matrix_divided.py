#!/usr/bin/python3
"""
   jsfjbfjffgfgjfrjjdfb
"""


def matrix_divided(matrix, div):
    """
       lsknklrgjkrjbgfjkdbj
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    if not isinstance(div, (int, float)):
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
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

            l1.append(round(b / div, 2))
        l0.append(l1)
    return l0
