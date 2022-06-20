#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divide = a / b
    except ZeroDivisionError:
        divide = 0
    finally:
        print("inside result: {}".format(divide))
    return divide
