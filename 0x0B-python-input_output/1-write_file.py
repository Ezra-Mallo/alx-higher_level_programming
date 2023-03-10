#!/usr/bin/python3
# 1-write_file.py
# ezra.mallo@gmail.com
"""Defines function that write to a text file"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) 

    and
    returns number of characters written

    Args:
        Filename = text file to write to
        text = string to be written

    Returns:
        Number of test written
    """

    with open(filename, "w") as my_file:
        count = my_file.write(str(text))

    my_file.closed
    return (count)
