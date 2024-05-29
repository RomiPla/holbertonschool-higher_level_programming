#!/usr/bin/python3
"""
    append task 2
"""


def append_write(filename="", text=""):
    """
        Funcion para escribir en un .txt file
    """
    with open(filename, "a", encoding="utf=8") as f:
        c = f.write(text)
    return c
