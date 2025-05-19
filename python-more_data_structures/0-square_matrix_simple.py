#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Return a matrix with all values squared from the original matrix."""
    return [[x ** 2 for x in row] for row in matrix]
