#!/usr/bin/python3
"""Import from models dirctory"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor

        Args:
            width (int): width of Rectangle
            height (int): height of Rectangle
            x (int): Defaults to 0.
            y (int): Defaults to 0.
            id (int, _type_): The number of instantiat of the base.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width Getter

        Returns:
            int: private attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Width Setter

        Args:
            value (int): Rectangle width value
        """
        self.__width = value

    @property
    def height(self):
        """Height Getter

        Returns:
            int: private attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Height Setter

        Args:
            value (int): Rectangle height value
        """
        self.__height = value

    @property
    def x(self):
        """X Getter

        Returns:
            int: private attribute x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """X Setter

        Args:
            value (int): Rectangle X value
        """
        self.__x = value

    @property
    def y(self):
        """Y Getter

        Returns:
            int: private attribute y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Y Setter

        Args:
            value (int): Rectangle Y value
        """
        self.__y = value
