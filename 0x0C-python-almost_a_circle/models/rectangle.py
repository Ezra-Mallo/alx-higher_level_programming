#!/usr/bin/python3
"""Base class"""

from models.rectangle import Base


class Rectangle(Base):
    """Implimenting Rectangle class"""

    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialisqtion """

        self.__width = width
        self.__height = height
        self.__x =  0
        self.__y = 0
        super().__init__()

     # using property decorator (getter function)
     @property
     def width(self):
         return self._width

     @property
     def height(self):
         return self._height

     @property
     def x(self):
         return self._x

     @property
     def y(self):
         return self._y

     #Setter functions
     @width.setter
     def width(self, value):
         self._width = value

     @height.setter
     def height(self, value):
         self._height = value

     @x.setter
     def x(self, value):
         self._x = value

     @y.setter
     def y(self, value):
         self._y = value
