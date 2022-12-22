#!/usr/bin/python3
"""
A module for a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """

    Args:
        matrix:
        div:

    Returns:

    """
    if matrix == []:
        return []
    if matrix is None:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    for i in matrix:
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")

    sizes = list(map(lambda x: len(x), matrix))
    if (len(set(sizes))) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = list(map(lambda x:
                      list(map(lambda y:
                               round(y / div, 2), x)), matrix))
    return result
