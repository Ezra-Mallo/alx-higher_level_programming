#!/usr/bin/python3
# 6-load_from_json_file.py
# ezra.mallo@gmail.com
"""Using a JSON representation"""

import json


def load_from_json_file(filename):
    """Function that creates an Object from a “JSON file”:

    Args:
        Filename:
    """

    with open(filename, 'r', encoding="utf-8") as my_file:
        a = my_file.read()
        return(json.loads(a))
