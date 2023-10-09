#!/usr/bin/python3
"""Module that holds Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from a BaseGeometry"""

    def __init__(self, width, height):
        """Initialize class
            Args:
                width: This for width rectangle
                height: This for height rectangle"""

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
