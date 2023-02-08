#!/usr/bin/python3
# 10-square.py
# ezra.mallo@gmail.com
""" Defines the instance of square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The geometric square shapei """

    def __init__(self, size):
        """Initialisation"""

        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)

    def area(self):
        """Compute area of a square"""

        return (self.__size ** 2)

    def __str__(self):
        """ Implementing str function"""

        return ("[Square] {}/{}".format(self.__size, self.__size))
