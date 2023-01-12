#!/usr/bin/python3
# 3-common_elements.py
# ezra.mallo@gmail.com


def common_elements(set_1, set_2):
    """Returns a set of common elements in two sets."""

    new_list = []
    for element in set_1:
        if element in set_2:
            new_list.append(element)

    return new_list
