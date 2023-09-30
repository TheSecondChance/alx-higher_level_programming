#!/usr/bin/python3
"""This for Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the integer addition two num a and b.

    Float arguments are to ints before addition is performed.

    Raises:
        TypeError: If of a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
