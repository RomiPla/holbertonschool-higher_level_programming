#!/usr/bin/python3
"""
	Esta funcion divide
	un texto segun ".", "?" y ":"
"""


def text_indentation(text):
    """
    Se divide una Str de texto
    segun la puntuacion . ? :
    como argumentos recibe un
    text(str) y si esta no es
    una str devuelve un Error
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    tx1 = text.replace('.', '.\n\n').replace('?', '?\n\n').replace(':', ':\n\n')
    tx = tx1.strip(" ")
    print("{:s}".format(tx))
