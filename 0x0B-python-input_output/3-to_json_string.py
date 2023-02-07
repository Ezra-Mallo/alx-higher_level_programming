#!/usr/bin/python3
# 3-to_json_string.py
# ezra.mallo@gmail.com
"""Defines function on json object"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)

    Args:
        my_obj: object to be represented json

    Returns:
        the object is returned in json format
    """

    return(json.dumps(str(my_obj)))
