#!/usr/bin/python3
"""
Defines a Function that adds two integers
Float arguments are typecasted to int before addition
Raises TypeError if a or b are not an integer or float
"""
def add_integer(a, b=98):
    """
    Function that adds 2 integers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
