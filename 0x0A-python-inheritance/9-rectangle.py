#!/usr/bin/python3
"""Module holds class BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherite from BaseGeometry Class """

    def __init__(self, width, height):
        """ Initializes class
        Args:
            width: width rectangle
            height: hegit rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Method that returr area instance"""
        return self.__width * self.__height

    def __str__(self):
        """Method that returns printable string"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
