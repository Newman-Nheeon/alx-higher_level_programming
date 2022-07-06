#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for ind_a in matrix:
        new_matrix[len(new_matrix):] = [[elem ** 2 for elem in ind_a]]
    return new_matrix
