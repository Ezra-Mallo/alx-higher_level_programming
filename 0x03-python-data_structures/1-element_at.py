#!/usr/bin/python3


def element_at(my_list, idx):
    """Write a function that retrieves an element from a list like in C."""

    k = 0
    for num in my_list:
        if k == idx:
            return num
        k += 1
