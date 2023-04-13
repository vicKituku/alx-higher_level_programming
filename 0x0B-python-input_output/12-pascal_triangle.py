#!/usr/bin/python3
"""Defines a function that returns a list of lists of
integers representing the Pascal’s triangle"""


def pascal_triangle(n):
    """ Returns a list of lists of integers representing
    Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle_list = [[1]]
    while len(triangle_list) != n:
        triangle = triangles[-1]
        temp = [1]
        for i in range(len(triangle) - 1):
            temp.append(triangle[i] + triangle[i + 1])
        temp.append(1)
        triangle_list.append(temp)
    return triangle_list
