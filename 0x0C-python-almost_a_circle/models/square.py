#!/usr/bin/python3


"""importing class Rectangle from its file"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inheriting Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializing class Square"""
        self.size = size
        self.__height = size
        self.__width = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returning dimensions of class Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.__width)

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        size = value
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be > 0")
        self.__width = size
        self.__height = size
        self.__size = size

    def update(self, *args, **kwargs):
        """kwargs and args update method"""
        if args is not None and len(args) != 0:
            self.id = args[0]
            if len(args) == 2:
                self.size = args[1]
            if len(args) == 3:
                self.x = args[2]
            if len(args) == 4:
                self.y = args[3]

        for n, j in kwargs.items():
            if n == "id":
                self.id = j
            elif n == "size":
                self.size = j
            elif n == "x":
                self.x = j
            elif n == "y":
                self.y = j
