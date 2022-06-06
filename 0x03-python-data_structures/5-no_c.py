#!/usr/bin/env python3
def no_c(my_string):
    zebby = [n for n in my_string if n != 'c' and n != 'C']
    return ("".join(zebby))
