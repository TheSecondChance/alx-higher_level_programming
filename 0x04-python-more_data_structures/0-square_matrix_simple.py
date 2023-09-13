#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for first1 in matrix:
        transpose = []
        for first in first1:
            first = first * first
            transpose.append(first)
        new_matrix.append(transpose)
    return new_matrix
