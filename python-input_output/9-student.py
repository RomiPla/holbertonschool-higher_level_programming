#!/usr/bin/python3
"""
    Modulo
"""


class Student:
    """
        clase student
    """
    def __init__(self, first_name, last_name, age):
        """
            init
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            To json
        """
        return self.__dict__
