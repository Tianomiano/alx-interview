#!/usr/bin/python3
"""
minOperations function which calculates,
the fewest number of operations needed,
to result in exactly n 'H' characters in a file.
"""


def minOperations(n):
    """
    factors n and finds the largest factor,
    that can be used to perform Paste operations,
    continuously reducing n until it reaches 1.
    """
    operations = 0
    min_operations = 2
    while n > 1:
        while n % min_operations == 0:
            operations += min_operations
            n /= min_operations
        min_operations += 1
    return operations
