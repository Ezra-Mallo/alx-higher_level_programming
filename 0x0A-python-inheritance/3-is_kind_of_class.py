#!/usr/bin/python3
# 3-is_kind_of_class.py
# ezra.mallo@gmail.com


def is_kind_of_class(obj, a_class):
    """Checks if obj is and instance of a class or subclass

    Args:
        obj: Object
        a_class: the class
    Returns:
        True: if is instance
        False: if not
        """

    if isinstance(obj, a_class):
        return (True)
    return (False)
