#!/usr/bin/python3
"""Module that empty base class BaseGeometry and empty class function
"""


class BaseGeometry:
    """Geometry Class
    """

    def area(self):
        """Calculate area
        Returns:
            area"""
        raise Exception("area() is not implemented")
