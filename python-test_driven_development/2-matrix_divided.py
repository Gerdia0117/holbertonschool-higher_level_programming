#!/usr/bin/python3
"""Module for matrix division function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a number.

    Args:
        matrix: List of lists of integers/float
        div: Number to divide by (integer or float)

    Returns:
        New matrix with divided elements rounded to 2 decimal places

    Raises:
        TypeError: If matrix is not list of lists of numbers,
                  or if rows have different sizes,
                  or if div is not number
        ZeroDivisionError: If div is zero
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/float"

    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError(err_msg)

    if not all(isinstance(num, (int, float))
               for row in matrix for num in row):
        raise TypeError(err_msg)

    if not matrix:
        return []

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
