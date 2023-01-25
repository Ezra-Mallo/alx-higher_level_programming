#!/usr/bin/python3
# 6-square-py
# ezra.malo@gmail.com
"""Define Square class"""


class Square:
    """Square that defines a square:"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialization"""

        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Property setter for the value for the size"""

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Retrieves position of square"""

        return self.__position

    @position.setter
    def position(self, value):
        """property setter to set position to a tuple"""

        if ((not isinstance(value, tuple)) or
                (len(value) != 2) or
                (not isinstance(value[0], int)) or
                (not isinstance(value[1], int)) or
                (not all(i >= 0 for i in value))):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

        #not all(isinstance(num, int) for num in value) can replace 44-45

    def area(self):
        """Compute Area"""

        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character i#"""

        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

        if self.__position[0] == 0:
            print()
