#!/usr/bin/python3
# 4-inherits_from.py
# ezra.mallo@gmail.com
"""Defines a function that checks only subclass of objects"""


def inherits_from(obj, a_class):
    """Returns True if object is an instance of a sub class

    that it inherited (directly or indirectly) from the specified

    class; otherwise False.

    Args:
        obj: Object
        a_class: Class of the object
    Return:
        True: if true or
        False: if false
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    return (False)
