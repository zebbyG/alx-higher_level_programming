#!/usr/bin/python3
""" create a class Square with attribute size assigned to value 0"""


class Square:
    """ Created a class Square with attribute size assigned to value zero"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size ** 2)
