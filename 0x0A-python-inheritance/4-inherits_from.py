#!/usr/bin/python3


"""
writing a funtion
"""


def inherits_from(obj, a_class):
    """
    prototype for the function
    """
    if type(obj) != a_class:
        return True
    if isinstance(obj, a_class):
        return False
    else:
        return False
