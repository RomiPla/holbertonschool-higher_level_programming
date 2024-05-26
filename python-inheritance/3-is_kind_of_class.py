#!/usr/bin/python3
"""
    Módulo que devuelve Verdadero si el objeto es una instancia de,
    o si el objeto es una instancia de una clase que heredó de,
    la clase especificada; de lo contrario, Falso.
"""


def is_kind_of_class(obj, a_class):
    """
        Verdadero si el objeto es una instancia de,
        o si el objeto es una instancia de una
        clase que heredó de la clase especificada;
        de lo contrario, Falso.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
