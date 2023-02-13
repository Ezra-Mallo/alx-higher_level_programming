#!/usr/bin/python3
# 9-student.py
"""Define Module"""

class Student:
    """Class Student that defines a student by"""

    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """Instatiation"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
