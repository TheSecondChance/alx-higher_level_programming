#!/usr/bin/python3
"""For 3-square Define the
class Square enao"""


class Square:
    """This for Represnt square
    """

    def __init__(self, size=0):
        """Initialize object for new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square
        public method the returns
        """
        return (self.__size * self.__size)
