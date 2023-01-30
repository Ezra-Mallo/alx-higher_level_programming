#!/usr/bin/python3
# 1-rectangle.py
# ezra.mallo@gmail.com
"""Represent a rectangle Class."""


class Rectangle:
    """Represent a rectangle."""
    self.width = 0

    def __init__(self, width=0, height=0):
        """Inititalization"""

        self.width = width
        self.height = height

    @property
    def width(self, value):
        """Retrieves width of rectangle"""

        return self.__width

    @width.setter
    def with(self, value):
        """Property setter for the value for the widht"""

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self, value):
        """Retrieves height of rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Property setter for the value for the height"""

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('iheight must be >= 0')
        self.__height = value
