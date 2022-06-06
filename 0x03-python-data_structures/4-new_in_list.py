#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    for i in range(len(my_list)):
        if (idx < 0) or (idx > len(my_list) - 1):
            return (my_list)

    copy = [z for z in my_list]
    copy[idx] = element
    return (copy)
