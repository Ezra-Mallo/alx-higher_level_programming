#!/usr/bin/python3
# 4-only_diff_elements.py
# ezra.mallo@gmail.com


def only_diff_elements(set_1, set_2):
    """Returns a set of different elements in two sets."""

    new_list = []
    for element in set_2:
        if element not in set_1:
            new_list.append(element)
    for element in set_1:
        if element not in set_2:
            new_list.append(element)

    return new_list
