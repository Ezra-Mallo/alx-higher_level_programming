#!/usr/bin/python3
# 1-my_list.py
# ezra.mallo@gmail.com
"""Defined a function that returns the list"""


class MyList(list):
    """ A class MyList that inherits from list
    Args:
        list
    """

    def print_sorted(self):
        """Print listed as sorted"""

        print(sorted(self))
