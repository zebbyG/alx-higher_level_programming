#!/usr/bin/python3


"""
function that returns JSON representation of an object
: importing json
"""


import json


def to_json_string(my_obj):
    """
    prototype for the function
    """
    return json.dumps(my_obj)
