#!/usr/bin/python3
# 2-uniq_add.py
# ezra.mallo@gmail.com


def uniq_add(my_list=[]):
    """Add all unique integers in a list."""

    new_list = []
    total = 0
    for item in my_list:
        if item not in new_list:
            new_list.append(int(item))
            total += item
    return (total)
