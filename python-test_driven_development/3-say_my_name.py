#!/usr/bin/python3
"""
	Este modulo imprime
	en pantalla nombre y apellido
"""


def say_my_name(first_name, last_name=""):
    """
    Di mi nombre- imprimir nombre en pantalla
    Argumentos de la funcion:
    str first_name- Nombre a imprimir
    str last_name- Apellido a imprimir
    Error de la funcion:
    si first_name y last_name no son strings = TypeError
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
