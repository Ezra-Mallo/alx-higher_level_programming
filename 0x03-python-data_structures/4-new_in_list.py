#!/usr/bin/python3


# 4-new_in_list.py
# ezra.mallo@gmail.com

def new_in_list(my_list, idx, element):
    """Function that replaces an element in a list at a specific position
    without modifying the original list (like in C)."""

    copy_new_list = my_list.copy()
    for i in range(len(copy_new_list)):
        if i == idx:
            copy_new_list[i] = element

    return copy_new_list
