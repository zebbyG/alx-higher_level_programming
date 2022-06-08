#!/usr/bin/python3
def uniq_add(my_list=[]):
    ret = []
    for z in set(my_list):
        ret += z
    return (ret)
