#!/usr/bin/python3
"""class Student that defines a studen"""


class Student:
    """create student class"""

    def __init__(self, first_name, last_name, age):
        """
        special method initialize
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrive the dict reprenting"""
        if attrs is None:
            return self.__dict__.copy()
        dicte = {}
        for i in attrs:
            if i in self.__dict__.keys():
                dicte[i] = self.__dict__[i]
        return dicte

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance
        """

        pwd_dict = self.__dict__
        for i in json.keys():
            for yalew_i in pwd_dict.keys():
                if i == yalew_i:
                    pwd_dict[yalew_i] = json[i]
        return yalew_i
