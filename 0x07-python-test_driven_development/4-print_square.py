#!/usr/bin/python3
"""Defines a function that prints a square"""
def print_square(size):
    """
    Prints a square with the character #

    param size: an integer representing the size length of the square
    raises TypeError: if size is not an integer or is a float less than 0
    raises ValueError: if size is less than 0
    return: None
    """
    if not isinstance(size, int):
        if isinstance(size, float) and size.is_integer():
            size = int(size)
        else:
            raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
