#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    new_d = a_dictionary.copy()
    if a_dictionary:
        new_d = max(a_dictionary, key=a_dictionary.get)
        return new_d
