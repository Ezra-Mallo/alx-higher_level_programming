#!/usr/bin/python3
# 9-student.py
"""Define Module"""


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

    def to_json(self):
        """Return dictionary of the file object"""

        return(self.__dict__)
