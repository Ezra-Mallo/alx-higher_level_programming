#!/usr/bin/python3
# 0-add_integer.py
# ezra.mallo@gmail.com


def add_integer(a, b=98):
    """Sum two numbers.


    Args:
        a (int): integer or float
        b (int): integer or float

    Returns: raise a TypeError if not integer or float
                 convert to integer if it is float
                 Sum of a, b
    Raises: TypeError

    Examples:
        >>> add_integer(3, 4)
        7
        >>> add_integer(3.0, 4.0)
        7

    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
