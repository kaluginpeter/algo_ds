import numpy as np

def fibonacci_number(n: int) -> int:
    """
    Retuning n'th fibonacci number, number can be negative.
    Using matrix multiplication.
    Time complexity O(log(N)).
    Example of usages:
    fibonacci_number(10) -> 55
    fibonacci_number(100) -> 354224848179261915075
    :param n:
    :return int:
    """
    matrix = np.matrix([[1, 1], [1, 0]], dtype=object) ** abs(n)
    if n % 2 == 0 and n < 0:
        return -matrix[0, 1]
    return matrix[0, 1]
