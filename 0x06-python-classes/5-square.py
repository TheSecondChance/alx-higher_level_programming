#!/usr/bin/python3
"""This for Define a class Square
"""


class Square:
    """Defines a square
    privae instance attribute size"""

    def __init__(self, size):
        """This for Initialize a new square
        size of the new square
        """
        self.size = size

    @property
    def size(self):
        """the object square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """This for the method to set"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Thsi for return the area of the object square."""
        return (self.__size * self.__size)

    def my_print(self):
        """this for print '#' the object square"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
