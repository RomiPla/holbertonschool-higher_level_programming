#!/usr/bin/python3
"""
   Módulo para guardar obj dentro del archivo
"""

import json


def save_to_json_file(my_obj, filename):
    """
        Funcion
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
