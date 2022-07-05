#!/usr/bin/python3


"""
writing a function that writes an object to a text file
"""

import json


def save_to_json_file(my_obj, filename):
    """
    prototype for the function
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
