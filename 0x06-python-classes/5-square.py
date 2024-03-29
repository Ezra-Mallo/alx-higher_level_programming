#!/usr/bin/python3
# 5-square-py
# ezra.malo@gmail.com
"""Define Square class"""


class Square:
    """Square that defines a square:"""

    def __init__(self, size=0):
        """Initialization"""

        self.__size = size

    @property
    def size(self):
        """Retrieves size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Compute Area"""

        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character i#"""

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
