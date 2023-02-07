#!/usr/bin/python3
# 4-inherits_from.py
# ezra.mallo@gmail.com


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class

    that inherited (directly or indirectly) from the specified

    class; otherwise False.
    """

    if issubclassof(obj, a_class):
        return (True)
    return (False)




