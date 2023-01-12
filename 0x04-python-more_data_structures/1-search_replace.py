#!/usr/bin/python3
# 1-search_replace.py
# ezra.mallo@gmail.com


def search_replace(my_list, search, replace):
    """Search and replaces all."""

    new_list = my_list.copy()
    for i in range(len(new_list)):
        item = new_list[i]
        if item == search:
            new_list[i] = replace
        else:
            new_list[i] = item

    return new_list
