#!/usr/bin/python3
# 10-square.py
# ezra.mallo@gmail.com
""" Defines the instance of square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The geometric square shapei """

    def __init__(self, size):
        """Initialisation"""

        self.__width = self.integer_validator("size", size)
        self.__height = self.integer_validator("size", size)

        super().__init__(size, size)
