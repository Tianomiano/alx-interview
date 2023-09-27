#!/usr/bin/python3
"""
an implementation of a function pascal_triangle(n) that generates
Pascal's Triangle up to the n-th level and returns it as a list of lists of numbers
"""

def pascal_triangle(n):
    """ This function will generate Pascal's Triangle up to level n """
    if n <= 0:
        return []

    """ list is initialized with n zeros """
    pascal_triangle = [0] * n

    for i in range(n):
        """ generate each row of Pascal's Triangle. """
        """ Pascal's Triangle rows have one more element than their row number """
        row = [0] * (i+1)
        row[0] = 1
        row[len(row) - 1] = 1

        for j in range(1, i):
            """ calculate the middle elements of the current row """
            if j > 0 and j < len(row):
                x = pascal_triangle[i - 1][j]
                y = pascal_triangle[i - 1][j - 1]
                row[j] = x + y

        pascal_triangle[i] = row

    return pascal_triangle