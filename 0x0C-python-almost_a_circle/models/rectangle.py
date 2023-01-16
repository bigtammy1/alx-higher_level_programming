#!/usr/bin/python3
""" My Rectangle class module """
from models.base import Base


class Rectangle(Base):
    """ My Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)

    @property
    def width(self):
        """ Gets the width of the Rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of the Rectangle """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Gets the height of the Rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of the Rectangle """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Gets the x value of the Rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets the x value of the Rectangle """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Gets the y value of the Rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets the x value of the Rectangle """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculates the area """
        return self.__width * self.__height

    def display(self):
        """ Prints a rectangle with # """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """ Updates a rectangle """
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.width = j
                elif i == 2:
                    self.height = j
                elif i == 3:
                    self.x = j
                elif i == 4:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ To Dictionary """
        result = {"x": self.__dict__["_Rectangle__x"],
                  "width": self.__dict__["_Rectangle__width"],
                  "id": self.__dict__["id"],
                  "height": self.__dict__["_Rectangle__height"],
                  "y": self.__dict__["_Rectangle__y"]}
        return result
