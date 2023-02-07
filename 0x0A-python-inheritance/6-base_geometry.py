#!/usr/bin/python3
# 6-base_geometry.py
# ezra.mallo@gmail.com
"""Defines an class of geometry"""


class BaseGeometry:
    """Class of BaseGeometry"""

    def area(self):
        """Function raises an Exception"""

        self.name = self

        raise Exception("area() is not implemented")
