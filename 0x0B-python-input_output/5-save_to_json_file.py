#!/usr/bin/python3
# 5-save_to_json_file.py
# ezra.mallo@gmail.com
"""Using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """Write an Object to a text file, using a JSON representation

    Args:
        my_obj(): to be writen
        Filename:
    """

    with open(filename, "w") as my_file:
        json.dump(my_obj, my_file)
