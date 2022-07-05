#!/usr/bin/python3
"""
function that creates an Object from a “JSON file
”"""


import json


def load_from_json_file(filename):
    """prototype for the function”"""
    with open(filename, 'r') as f:
        z = json.load(f)
        return z
