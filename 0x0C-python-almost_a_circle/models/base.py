#!/usr/bin/python3
""" My base class module """
import json


class Base:
    """ My Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization method """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Converts to a json string """
        if list_dictionaries is not None or len(list_dictionaries) != 0:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """ Saves json to a file """
        lobjs = []
        sobjs = []
        for i in list_objs:
            if i.__class__.__name__ == "Rectangle":
                lobjs.append(i.to_dictionary())
            elif i.__class__.__name__ == "Square":
                sobjs.append(i.to_dictionary())
        if lobjs:
            with open("Rectangle.json", "w") as f:
                f.write(Base.to_json_string(lobjs))
        if sobjs:
            with open("Square.json", "w") as f:
                f.write(Base.to_json_string(sobjs))

    @staticmethod
    def from_json_string(json_string):
        """ changes from json to a list """
        if not json_string or json_string is not None:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """ Creates an instance with all the attributes already set """
        dummy = None
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        FILENAME = "{}.json".format(cls.__name__)
        instances = []
        with open(FILENAME, "r") as f:
            file_list = Base.from_json_string(f.read())
            for i in file_list:
                instances.append(cls.create(**i))
        return instances
