#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
    divides all elements in a matrix
    """
    if (not isinstance(matrix, list) or mattrix == [] or 
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(element1, int) or isinstance(element1, float))
                    for element1 in [num for row in matrix for num in row])):
        raise TypeError("matrix must bea matrix (list of lists) of integers/ floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise Type Error("Each row of the matrix must have the same size")


    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division is zero")
    

    return ([list(map(lambda x: round(x / div,2), row)) for row in matrix])
