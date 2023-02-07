#!/usr/bin/python3
# 2-append_write.py
# ezra.mallo@gmail.com
"""Defines function that append to a text file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)


    and

    returns number of characters written

    Args:
        Filename = text file to write to
        text = string to be written

    Returns:
        Number of test written
    """

    with open(filename, "a") as my_file:
        count = my_file.write(str(text))

    my_file.closed
    return (count)
