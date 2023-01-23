#!/usr/bin/python3
# 0-safe_print_list.py
# ezra.mallo@gmail.com


def safe_print_list(my_list=[], x=0):
    """Function that prints x elements of a list."""
    try:
        new_val = ""
        for i in my_list[:x]:
            new_val += str(i)
            print("{}".format(new_val))
        return int(new_val)
    except ValueError:
        print(ValueError)
