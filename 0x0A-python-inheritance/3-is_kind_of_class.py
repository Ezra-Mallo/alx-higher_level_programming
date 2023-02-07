#!/usr/bin/python3
# 3-is_kind_of_class.py
# ezra.mallo@gmail.com


def is_same_class(obj, a_class):
    """Returns True if the object = an instance of the specified class
    or

    Args:
        obj: Object
        a_class: the class
    Returns:
        True: if is instance
        False: if not

    otherwise False."""

    if type(obj) == a_class:
        return (True)
    return (False)
