#!/usr/bin/python3
""" creating class LockedClass """


class LockedClass:
    """
    LockedClass not to allow any other attributes
    """
    __slots__ = ['first_name']
