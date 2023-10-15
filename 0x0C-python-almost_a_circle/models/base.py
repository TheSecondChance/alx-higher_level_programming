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

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): list of dictionaries

        Returns:
            list: Return the JSON serialization
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON encoding a list of objects to a file

        Args:
            list_objs (list): list of instances who inherits of Base_
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                file.write(Base.to_json_string(list_dicts))
