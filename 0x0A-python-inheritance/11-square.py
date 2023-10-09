#!/usr/bin/python3
"""Module that holds the class Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class inherites from Rectangle Rectangle"""

    def __init__(self, size):
        """Method Initializes Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """this return a string has a area"""
        return super().area()

    def __str__(self):
        """Method return square printable string"""
        return "[Square] {}/{}".format(self.__size, self.__size)
