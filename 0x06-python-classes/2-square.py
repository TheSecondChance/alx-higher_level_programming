#!/usr/bin/python3
"""This for Define class Square
"""


class Square:
    """This for Reprent a square
    """

    def __init__(self, size=0):
        """This for Initialize new Square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
