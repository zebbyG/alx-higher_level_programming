#!/usr/bin/python3
""" create a class Square with attribute size assigned to value 0"""


class Square:
    """ Created a class Square with attribute size assigned to value zero"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        size = value
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for z in range(0, self.__position[1]):
            print()
        for e in range(0, self.__size):
            for b in range(0, self.__position[0]):
                print(" ", end="")
            for y in range(0, self.__size):
                print("#", end="")
            print()
