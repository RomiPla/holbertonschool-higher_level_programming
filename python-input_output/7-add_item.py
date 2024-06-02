#!/usr/bin/python3
"""
    Módulo que añade todos los argumentos a una lista de Python,\
    y luego los guarda en un archivo.
"""

from sys import argv
"""
    import argv
"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

open("add_item.json", "a")
try:
    f = load_from_json_file("add_item.json") + argv[1:]
    save_to_json_file(f, "add_item.json")
except ValueError:
    save_to_json_file(argv[1:], "add_item.json")
