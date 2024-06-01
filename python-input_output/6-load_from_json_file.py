#!/usr/bin/python3
"""
    Modulo para crear un obj desde un archivo json
"""

import json


def load_from_json_file(filename):
    """
        Funcion
    """

    with open(filename, encoding="utf-8") as f:
        """open"""
        return (json.loads(f.read()))
