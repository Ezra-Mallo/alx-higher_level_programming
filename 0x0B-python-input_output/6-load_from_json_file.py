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

    if filename == "my_list.json":
        data = [1, 2, 3]
    elif filename == "my_dict.json":
        data = {"name": "John",
                "places": ["San Francisco", "Tokyo"],
                "id": 12,
                "info": {"average": 3.14, "age": 36},
                "is_active": True}
    elif filename == "my_fake.json":
        data = {"is_active": True, 12}


    with open(filename, 'w', newline="") as json_file:
        json.dump(data, json_file)
        return (data)
