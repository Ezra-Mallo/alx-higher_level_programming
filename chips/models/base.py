#!/usr/bin/python3
"""Base class"""


class Base:
    """Implimenting Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialisqtion """

        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
