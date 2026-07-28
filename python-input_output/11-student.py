#!/usr/bin/python3
"""Module that defines a Student class with (de)serialization support."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): the student's first name.
            last_name (str): the student's last name.
            age (int): the student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of this Student.

        Args:
            attrs (list): optional list of attribute names (str) to
                retrieve. If not a list of strings, all attributes
                are retrieved.

        Returns:
            dict: the selected attributes of this Student.
        """
        if type(attrs) is list and all(type(a) is str for a in attrs):
            return {
                key: value for key, value in self.__dict__.items()
                if key in attrs
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of this Student from a dictionary.

        Args:
            json (dict): a dictionary mapping attribute names to
                their new values.
        """
        for key, value in json.items():
            setattr(self, key, value)
