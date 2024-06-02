#!/usr/bin/env python3
import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializa la instancia actual del objeto y la guarda en el nombre de archivo proporcionado.

        Parámetros:
        filename (str): El nombre del archivo pickle de salida.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"An error occurred during serialization: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Carga y devuelve una instancia de CustomObject desde el nombre de archivo proporcionado.

        Parámetros:
        filename (str): El nombre del archivo pickle de entrada.

        Devuelve:
        CustomObject: Una instancia de CustomObject si la deserialización es exitosa, de lo contrario None.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print(f"An error occurred during deserialization: {e}")
            return None

if __name__ == "__main__":
    obj = CustomObject(name="John", age=25, is_student=True)
    print("Original Object:")
    obj.display()

    obj.serialize("object.pkl")

    new_obj = CustomObject.deserialize("object.pkl")
    print("\nDeserialized Object:")
    if new_obj:
        new_obj.display()
    else:
        print("Failed to deserialize the object.")
