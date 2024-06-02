#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializa un diccionario de Python en XML y lo guarda en el nombre de archivo proporcionado.

    Parámetros:
    dictionary (dict): El diccionario a serializar.
    filename (str): El nombre de archivo para guardar los datos XM
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    try:
        tree.write(filename)
        return True
    except Exception as e:
        print(f"An error occurred during serialization: {e}")
        return False

def deserialize_from_xml(filename):
    """
    Deserializa datos XML de un nombre de archivo dado en un diccionario de Python.

    Parámetros:
    filename (str): El nombre del archivo XML para leer.

    Devuelve:
    dict: El diccionario deserializado.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        result = {}
        for child in root:
            result[child.tag] = child.text
        
        return result
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None
    except ET.ParseError as e:
        print(f"An error occurred during deserialization: {e}")
        return None

if __name__ == "__main__":
    def main():
        sample_dict = {
            'name': 'John',
            'age': '28',
            'city': 'New York'
        }

        xml_file = "data.xml"
        if serialize_to_xml(sample_dict, xml_file):
            print(f"Dictionary serialized to {xml_file}")

        deserialized_data = deserialize_from_xml(xml_file)
        print("\nDeserialized Data:")
        print(deserialized_data)

    main()
