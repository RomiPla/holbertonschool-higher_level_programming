#!/usr/bin/python3
"""
    Task 0
"""


def read_file(filename=""):
    """
       Funcion que imprime un .txt file
    """
    with open(filename, "rt", encoding="utf=8") as f:
        for line in f.read():
            print(line, end="")
