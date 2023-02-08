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
        """Validate value
        Args:
            name(str): name of the object
            value(int): int value
        Raises:
            TypeError: when val != int
            ValueError: value <= 0
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{} must be greater than 0".format(name))
