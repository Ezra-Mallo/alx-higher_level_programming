#!/usr/bin/python3
# 9-multiply_by_2.py
# ezra.mallo@gmail.com


def multiply_by_2(a_dictionary):
    """Function that returns a new dictionary value multiplied by 2"""

    return {key: val * 2 for key, val in a_dictionary.items()}
