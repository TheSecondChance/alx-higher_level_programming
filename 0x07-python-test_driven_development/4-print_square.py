#!/usr/bin/python3
"""
This Module 4-print_square
contains a function that prints out a square using the '#' char
"""


def print_square(size):
    """prints a square with the # char
    Args:
        size: size of the square to be printed
    Returns:
        No return
    Raises:
        TypeError: if size is not an int
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)

