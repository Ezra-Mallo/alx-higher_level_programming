#!/usr/bin/python3
# 7-base_geometry.py
# ezra.mallo@gmail.com
"""Defines an class of geometry"""


class BaseGeometry:
    """Class of BaseGeometry"""

    def area(self):
        """Function raises an Exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value

        Args:
            name(str): name of the object
            value(int): value of the object
        Raises:
            TypeError: if not integer
            ValueError: if <=0
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))

        self.name = name
        self.value = value
