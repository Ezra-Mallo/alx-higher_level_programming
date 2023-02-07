#!/usr/bin/python3
# 2-is_same_class.py
# ezra.mallo@gmail.com
"""Defines a function that returns True  for an exact instance"""


def is_same_class(obj, a_class):
    """Returns True if the object = an instance of the specified class
        or otherwise False

    Args:
        obj: Object
        a_class: the class
    Returns:
        True: if is instance
        False: if not
    """

    if type(obj) == a_class:
        return (True)
    return (False)
