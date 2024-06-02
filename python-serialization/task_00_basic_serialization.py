#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Parámetros:
    data (dict): El diccionario de Python a serializar.
    filename (str): El nombre del archivo JSON de salida. Si el archivo de salida ya existe, será reemplazado.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Carga y deserializa datos desde un archivo JSON a un diccionario de Python.

    Parámetros:
    filename (str): El nombre del archivo JSON de entrada.

    Devuelve:
    dict: Un diccionario de Python con los datos deserializados del JSON.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    data_to_serialize = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    serialize_and_save_to_file(data_to_serialize, 'data.json')

    print("Data serialized and saved to 'data.json'.")

    deserialized_data = load_and_deserialize('data.json')

    print("Deserialized Data:")
    print(deserialized_data)
