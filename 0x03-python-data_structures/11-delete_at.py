#!/usr/bin/python3
# 11-delete_at.pyi
# ezra.mallo@gmail.com


def delete_at(my_list=[], idx=0):
    """Function that deletes the item at a specific position in a list."""

    if idx >= 0 and idx < len(my_list):
        del my_list[idx]

    return my_list
