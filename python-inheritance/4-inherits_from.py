#!/usr/bin/python3
"""
   Módulo para verificar si obj es
   una instancia de una clase heredada de a_class.
"""


def inherits_from(obj, a_class):
    """
        Verdadero si el objeto es una instancia de una clase que heredó
        (directa o indirectamente) de la clase especificada;
        de lo contrario, Falso.
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True

    else:
        return False
