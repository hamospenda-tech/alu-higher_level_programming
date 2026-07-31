#!/usr/bin/python3
"""Module that defines the Base class for all other classes in the project"""
import json


class Base:
    """Base class that manages the id attribute for all derived classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base instance with an id.

        Args:
            id (int): the id to assign; if None, uses the objects counter.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): a list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): a list of instances that inherit from Base.
        """
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list represented by a JSON string.

        Args:
            json_string (str): a JSON string representing a list of dicts.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Args:
            **dictionary: key/value pairs of attributes to set.
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances loaded from <Class name>.json"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as f:
                list_dicts = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []
        return [cls.create(**d) for d in list_dicts]
