#!/usr/bin/python3
# 4-from_json_string.py
# ezra.mallo@gmail.com
"""Defines function on json object"""
import json


def from_json_string(my_str):
    """Write a function that returns an object (Python data structure)

    represented by a JSON string:


    Args:
        my_str json parameter

    Returns:
        string
    """

    return(json.loads(my_str))
