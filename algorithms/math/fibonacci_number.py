import sys
import decimal
from functools import lru_cache

import numpy as np


def fibonacci_number_matrix_multiplication(n: int) -> int:
    """
    Retuning n'th fibonacci number, number can be negative.
    Using matrix multiplication.
    Time complexity O(log(N)).
    Example of usages:
    fibonacci_number_matrix_multiplication(10) -> 55
    fibonacci_number_matrix_multiplication(100) -> 354224848179261915075
    :param n:
    :return int:
    """
    matrix = np.matrix([[1, 1], [1, 0]], dtype=object) ** abs(n)
    if n % 2 == 0 and n < 0:
        return -matrix[0, 1]
    return matrix[0, 1]


sys.setrecursionlimit(5000)


@lru_cache()
def fibonacci_number_recursive(n: int) -> int:
    """
    Retuning n'th fibonacci number, n can be negative.
    Using recursive implementation with memoization.
    Time complexity O(N).
    Example of usages:
    fibonacci_number_recursive(10) -> 55
    fibonacci_number_recursive(100) -> 354224848179261915075
    :param n:
    :return int:
    """
    n = abs(n)
    if n == 1 or n == 2:
        return 1
    return fibonacci_number_recursive(n - 1) + fibonacci_number_recursive(n - 2)


def fibonacci_number_iterative(n: int) -> int:
    """
    Retuning n'th fibonacci number, n can be negative.
    Using recursive iterative straight forward implementation.
    Time complexity O(N).
    Example of usages:
    fibonacci_number_iterative(10) -> 55
    fibonacci_number_iterative(100) -> 354224848179261915075
    :param n:
    :return int:
    """
    n = abs(n)
    a: int = 0
    b: int = 1
    for i in range(n):
        a, b = b, a + b
    return a


def fibonacci_number_bine(n: int) -> int:
    """
    Retuning n'th fibonacci number, n can be negative.
    Using Bine formula.
    Time complexity O(log(N)).
    Example of usages:
    fibonacci_number_bine(10) -> 55
    fibonacci_number_bine(100) -> 354224848179261915075
    :param n:
    :return int:
    """
    decimal.getcontext().prec = 300_000
    n = abs(n)
    root_5: float = decimal.Decimal(5).sqrt()
    phi: float = (1 + root_5) / 2
    x: int = round(((phi ** n) - ((-phi) ** -n)) / root_5)
    return x
