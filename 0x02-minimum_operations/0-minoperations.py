#!/usr/bin/python3
"""
Minimum operations
"""


def minOperations(n):
    """
    In a text file, there is a single character H.
    Your text editor can execute only two operations in this file:
    Copy All and Paste. Given a number n, write a method that
    calculates the fewest number of operations needed to result
    in exactly n H characters in the file.
    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0
    """
    if n <= 1:
        return 0

    operations = [float('inf')] * (n + 1)
    operations[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                operations[i] = min(operations[i], operations[j] + i // j)

    return operations[n] if operations[n] != float('inf') else 0
