#!/usr/bin/python3
"""
gguregurkgrndjfrn
"""

import csv
import json
import os


class Base:
    """dkrdkdkrtjfhdud
    """
    __n_objects = 0

    def __init__(self, id=None):
        """kdkdridkfd
        """

        if id is not None:
            self.id = id

        else:
            Base.__n_objects += 1
            self.id = Base.__n_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """kdkfdufudjdjrk
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """jdjfufidkcjfif
        """

        list_objects = []
        if list_objs is None or len(list_objs) is 0:
            list_objects = []

        else:

            for i in list_objs:
                list_objects.append(i.to_dictionary())
        json_string = Base.to_json_string(list_objects)
        with open("{}.json".format(cls.__name__), mode='w',
                  encoding='utf-8') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """jdkxjfufidkc
        """

        if json_string is None or json_string is "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """kdkckjfidoclcld
        """

        from models.rectangle import Rectangle
        from models.square import Square

        if cls == Rectangle:
            dummy = cls(1, 1)
        if cls == Square:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """kskxkfiixkckjf
        """
        i_l = []
        fn = "{}.json".format(cls.__name__)
        if os.path.isfile(fn):
            with open(fn) as a:
                instance_object = cls.from_json_string(a.read())
                for i_d in instance_object:
                    i_l.append(cls.create(**i_d))
                return i_l
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save to file csv"""

        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Load from file csv"""

        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
