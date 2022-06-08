#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for z in range(len(my_list)):
        if my_list[z] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[z])
    return new_list
