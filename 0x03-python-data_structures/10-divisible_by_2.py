#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiples = []
    for z in range(len(my_list) - 1):
        if my_list[z] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)
            return multiples
