#!/usr/bin/python3

# 11-multiply_list_map.py
# ezra.mallo@gmail.com


def multiply_list_map(my_list=[], number=0):
    """Function that returns a list with all values

    multiplied by a number without using any loops."""

    return (list(map(lambda x: x * number, my_list)))
