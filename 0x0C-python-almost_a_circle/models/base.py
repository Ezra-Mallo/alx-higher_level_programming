#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """Implimenting Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base.

        Args:
            id (str): First Param
        Raises:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """JSON the standard formats for sharing data representation.

        Args:
            List
        """

        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))
