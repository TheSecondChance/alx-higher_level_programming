#!/usr/bin/python3
"""Module hold the class Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class inherits from Rectangle a Square"""

    def __init__(self, size):
        """Initializes a Square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ Method that returns a string with the area """
        return super().area()
