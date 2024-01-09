#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n"""
    if n <= 0:
        return []
    triangles = [[1]]
    while len(triangles) != n:
        a = triangles[-1]
        b = [1]
        for i in range(len(a) - 1):
            b.append(a[i] + a[i + 1])
        b.append(1)
        triangles.append(b)
    return triangles
