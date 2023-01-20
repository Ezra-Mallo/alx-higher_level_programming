#!/usr/bin/python3
# 102-complex_delete.py
# ezra.mallo@gmail.com


def complex_delete(a_dictionary, value):
    """Function that deletes keys with a specific value in a dictionary."""

    if value is None:
        return (a_dictionary)

    my_list = []
    for k, v in a_dictionary.items():
        if value == v:
            my_list.append(k)
    if len(my_list) == 0:
        return (a_dictionary)

    for key in my_list:
        if key in a_dictionary:
            del a_dictionary[key]

    return a_dictionary
