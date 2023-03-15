#!/usr/bin/python3
# Author: Victor Mwangangi
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(lambda x: x**2, row)))
    return new_matrix
