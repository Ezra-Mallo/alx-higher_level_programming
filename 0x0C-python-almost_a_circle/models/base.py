#!/usr/bin/python3
"""Base class"""


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
