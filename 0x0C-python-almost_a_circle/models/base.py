#!/usr/bin/python3
"""Module contains class Base"""


class Base:
    """The base model for all other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a base

        Args:
            id (int): The number of instantiat of base. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
