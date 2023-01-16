#!/usr/bin/python3
""" Module for Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes a square """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ Returns a string repr of a square """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    @property
    def size(self):
        """ Returns the size """
        return self.height

    @size.setter
    def size(self, value):
        """ Sets the size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Updates a Square """
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.size = j
                elif i == 2:
                    self.x = j
                elif i == 3:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ To Dictionary """
        result = {"id": self.__dict__["id"],
                  "x": self.__dict__["_Rectangle__x"],
                  "size": self.__dict__["_Square__size"],
                  "y": self.__dict__["_Rectangle__y"]}
        return result
