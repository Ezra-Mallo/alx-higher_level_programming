#!/usr/bin/python3
# 0-lookup.py
# ezra.mallo@gmail.com


def lookup(obj):
    """Returns the list of available attributes and methods of an object:

        Args:
            obj: Objects
        Returns: List
    """
    return (dir(obj))
