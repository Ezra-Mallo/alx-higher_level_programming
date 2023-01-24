#!/usr/bin/python3
# 0-square-py
# ezra.malo@gmail.com
"""Define Square class"""


class Square:
    """Square that defines a square:"""

    def __init__(self,  size=0):
        self.__size = size

        try:
            if isinstance(self.__size, int) is False:
                raise TypeError
            if self.__size <=0:
                raise ValueError
        except ValueError:
            print("size must be >= 0")
        except TypeError:
            print("size must be an integer")
