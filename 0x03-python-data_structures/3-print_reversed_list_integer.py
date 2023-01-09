#!/usr/bin/python3
# 3-print_reversed_list_integer.py
# ezra.mallo@gmail.com


def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list in reverse order."""

    if isinstance(my_list, list):
        my_list.reverse()
        for num in my_list:
            print("{:d}".format(num))
