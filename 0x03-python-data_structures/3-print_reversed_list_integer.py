#!/usr/bin/python3
def print_reversed_list_integer(mylist):
    for i in range(len(mylist)):
        if (mylist is not None):
            mylist.reverse()
            print(mylist[i])
