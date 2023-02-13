#!/usr/bin/python3
# 10-student.py
"""Defines Module"""


class Student:
    """Class Student that defines a student by"""

    def __init__(self, first_name, last_name, age):
        """Instatiation
        Args:
            first_name(str): first arguemnt
            last_name(str): 2nd arguement
            age (int): 3rd airguement
        Raises: None
        Returns: None
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary of the file object"""

        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            return self.__dict__
