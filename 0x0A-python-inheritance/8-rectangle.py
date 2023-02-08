#!/usr/bin/python3
# 7-base_geometry.py
# ezra.mallo@gmail.com
"""Defines an class of geometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class inherits BaseGeometry"""

    def __init__(self, width, height):
        """Initialization of attributes"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
