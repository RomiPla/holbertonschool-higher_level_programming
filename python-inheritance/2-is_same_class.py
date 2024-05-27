#!/usr/bin/python3
"""
    Módulo para verificar si obj es
    de la clase pasada
"""


def is_same_class(obj, a_class):
    """
        Verdadero si el objeto es
        exactamente una instancia de la
        clase especificada.
        De lo contrario, Falso.

    """
    if type(obj) is a_class:
        return True
    else:
        return False
