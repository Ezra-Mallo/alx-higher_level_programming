#!/usr/bin/python3
# 0-read_file.py
# ezra.mallo@gmail.com
"""Defines function that reads a text file"""


def read_file(filename=""):
    """Read a text file (UTF8) and prints it to stdouti

    Args:
        filename:
    """

    with open(filename) as my_file:
        for line in my_file:
            print(line, end="")

    my_file.closed
