#!/usr/bin/python3
"""Defines a function that divides all the numbers in a matrix with a given number"""
def matrix_divided(matrix, div):
    """Function accepts a matrix and a number
    It divides all the numbers in the matrix by the given number
    Returns a new matrix holding results of the division
    """
    # Check if the matrix is a list of lists of integers/floats
    if not all(isinstance(row, list) and all(isinstance(x, (int, float)) for x in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if each row of the matrix has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Divide each element of the matrix by div and round the result to 2 decimal places
    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    
    return new_matrix

