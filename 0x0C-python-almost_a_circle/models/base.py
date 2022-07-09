#!/usr/bin/python3


"""creating class base"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """function for class base"""
        self.id = id
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            Base.__nb_objects = self.id
