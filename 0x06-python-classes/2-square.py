#!/usr/bin/python3
# 0-square-py
# ezra.malo@gmail.com
"""Define Square class"""


class Square:
    """Square that defines a square:"""

    def __init__(self, size=0):
        """Initialization"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
