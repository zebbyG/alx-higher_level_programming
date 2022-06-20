#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    divide = []
    list_divide = 0
    for z in range(list_length):
        try:
            list_divide = my_list_1[z] / my_list_2[z]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            pass
        divide.append(list_divide)
    return divide
