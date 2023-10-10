#!/usr/bin/python3
""" that returns a list of lists of integers representing
the Pascal’s triangle of n"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        angle = triangle[-1]
        gizyawi = [1]
        for i in range(len(angle) - 1):
            gizyawi.append(angle[i] + angle[i + 1])
        gizyawi.append(1)
        triangle.append(gizyawi)
    return triangle
