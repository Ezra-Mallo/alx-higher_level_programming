#!/usr/bin/python3
# 102-complex_delete.py
#ezra.malo@gmail.com

def complex_delete(a_dictionary, value):
    """Function that deletes keys with a specific value in a dictionary."""

    my_list = []
    for k, v in a_dictionary.items():
        if value == v:
            my_list.append(k)
    for key in my_list:
        if key in a_dictionary:
            del a_dictionary[key]

    return a_dictionary
