#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    xcount = 0
    for n in range(x):
        try:
            print(f"{my_list[n]}", end="")
            xcount += 1
        except Exception as error:
            break
    print()
    return xcount
