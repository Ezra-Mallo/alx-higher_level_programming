#!/usr/bin/python3
"""Base class"""
from models.base import Base


class Rectangle(Base):
    """Implimenting Rectangle class"""

    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialisqtion """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the height of the Rectangle."""
        if type(value) != int:
            raise TypeError("Width must be an integer.")
        if value <= 0:
            raise ValueError("Width must be > 0.")
        self._width = value

    @property
    def height(self):
        """Set the height of the Rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle."""
        if type(value) != int:
            raise TypeError("Height must be an integer.")
        if value <= 0:
            raise ValueError("Height must be > 0.")
        self._height = value

    @property
    def x(self):
        """Get the x of the Rectangle."""
        return self._x

    @x.setter
    def x(self, value):
        """Set/get the width of the Rectangle."""
        if type(value) != int:
            raise TypeError("x must be an integer.")
        if value < 0:
            raise ValueError("x must be >= 0.")
        self._x = value


    @property
    def y(self):
        """Get the y of the Rectangle."""
        return self._y

    @y.setter
    def y(self, value):
        """Set the y of the Rectangle."""
        if type(value) != int:
            raise TypeError("y must be an integer.")
        if value < 0:
            raise ValueError("y must be >= 0.")
        self._y = value
