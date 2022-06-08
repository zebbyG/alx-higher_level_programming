#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[z ** 2 for z in row] for row in matrix]
    return new_matrix
