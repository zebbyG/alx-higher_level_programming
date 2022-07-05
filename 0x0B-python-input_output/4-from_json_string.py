#!/usr/bin/python3


"""
function that returns an object
:importing json
"""

import json


def from_json_string(my_str):
    """
    prototype for the function
    """
    z = json.loads(my_str)
    return z
