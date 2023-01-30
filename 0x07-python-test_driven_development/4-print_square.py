#!/usr/bin/python3
# 4-print_square.py
# ezra.mallo@gmail.com


def print_square(size):
    """Prints a square with the character #

    Args:
        size: interger

    Returns: nothing

    Raises:
        TypeError: size must be an integer (If size is not integer)
        ValueError: size must be >= 0 (if size is less than 0)
        TypeError : size must be an integer(if size is a float/less than 0)

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if not (size >= 0):
        raise ValueError("size must be >= 0")
    if isinstance(size, float):
        raise TypeError("size must be an integer")

    for row in range(size):
        print("#" * size)
