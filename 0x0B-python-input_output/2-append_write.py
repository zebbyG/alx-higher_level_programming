#!/usr/bin/python3


"""
writing a function that appends a string and returns the number of characters
"""


def append_write(filename="", text=""):
    """
    prototype for the function
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
