#!/usr/bin/python3
# 1-write_file.py
# ezra.mallo@gmail.com
"""Defines function that write to a text file"""


def write_file(filename="", text=""):
    """Read a text file (UTF8) and prints it to stdouti

    Args:
        filename:
    """

    with open(filename, "w") as my_file:
        count = my_file.write(str(text))

    my_file.closed
    return (count)
