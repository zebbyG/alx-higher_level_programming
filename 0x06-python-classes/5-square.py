#!/usr/bin/python3
""" create a class Square with attribute size assigned to value 0"""


class Square:
    """ Created a class Square that prints a square in stdout"""
    def _init_(self, size=0):
        self.size = size

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

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print("")
        for z in range(self.__size):
            print("#" * self.__size)
