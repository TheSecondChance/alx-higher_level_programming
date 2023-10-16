#!/usr/bin/python3
"""Module contains class Base"""
import json
import csv


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
        if list_dictionaries is None or list_dictionaries == "[]":
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

    @staticmethod
    def from_json_string(json_string):
        """decoding a JSON string

        Args:
            json_string (str):  JSON str representation of a list of dicts

        Returns:
            list represented by json_string
        """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """instance with all attributes already set

        Returns:
            dict: an instance with all attributes
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """instantiated from a file of JSON strings.

        Returns:
            dict: returns a list of instances
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as file:
                list_dicts = Base.from_json_string(file.read())
                return [cls.create(**dic) for dic in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV

        Args:
            list_objs (CSV): CSV serialization of a list of objects to a file.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes

        Returns:
            list: Return a list of classes instantiated from a CSV file.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(file, fieldnames=fieldnames)
                list_dicts = [
                    dict([key, int(value)] for key, value in dic.items())
                    for dic in list_dicts
                ]
                return [cls.create(**dic) for dic in list_dicts]
        except IOError:
            return []
