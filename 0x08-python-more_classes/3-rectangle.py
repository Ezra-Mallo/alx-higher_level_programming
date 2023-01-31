#!/usr/bin/python3
# 3-rectangle.py
# ezra.mallo@gmail.com
""" Rectangle class"""


class Rectangle:

    def __init__(self, width=0, height=0):
        """Initialization

        Args:
            width: integer
            height: integer
        Raises:
            TypeError: if width or height is not int
            ValueError: if width or height is < 0
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width"""

i        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Getter for height"""

        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ Compute Area"""

        return (self.__width * self.__height)

    def perimeter(self):
        """ Compute perimeter"""

        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__width + self.height))

    def __str__(self):
        """Str"""

        my_str = []
        for h in range(self.__height):
            for w in range(self.__width):
                my_str.append("#")
            my_str.append("\n")
        return ("".join(my_str))
