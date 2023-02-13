#!/usr/bin/python3
# 100-append_after.py
"""Defines text Search and replace."""


def append_after(filename="", search_string="", new_string=""):
    """Search and replace a string in a file.
    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename, "r") as read_file:
        for line in read_file:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w") as write_file:
        write_file.write(text)
