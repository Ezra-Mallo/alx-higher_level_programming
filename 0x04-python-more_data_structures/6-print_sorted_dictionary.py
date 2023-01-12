#!usr/bin/python3
# 6-print_sorted_dictionary.py
# ezra.mallo@gmail.com


def print_sorted_dictionary(a_dictionary):
    """Function that prints a dictionary by ordered keys."""

    for k in sorted(a_dictionary):
        print("{}: {}".format(k, a_dictionary[k]))
