#!/usr/bin/python3
# 4-rectangle.py
# ezra.mallo@gmail.com
"""Represent a rectangle Class."""


class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height of rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Property setter for the value for the height"""

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Compute area"""

        return (self.__width * self.__height)

    def perimeter(self):
        """Compute perimeter"""

        if self.width == 0 or self.height == 0:
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.

        """
        if self.width == 0 or self.__height == 0:
            return ("")
        my_str = []
        for h in range(self.__height):
            for w in range(self.__width):
                my_str.append(str(self.print_symbol))
            if h < self.__height-1:
                my_str.append("\n")
        return ("".join(my_str))


    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1