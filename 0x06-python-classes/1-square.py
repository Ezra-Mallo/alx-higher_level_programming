#!/usr/bin/python3
# 0-square-py
# ezra.malo@gmail.com
"""Define Square class"""


class Square:
    """Square that defines a square:"""

    def __init__(self, name, size=0):
        self.name = name
        self.__size = size
