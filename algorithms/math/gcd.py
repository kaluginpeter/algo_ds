def gcd_euclidian(x: int, y: int) -> int:
    """
    Return greatest common divisor of both elements.
    Use Euclidian algorithm.
    Time complexity is O(log(N)).
    Memory complexity is O(1).
    Example of usages:
    a = 10
    b = 20
    gcd_euclidian(a, b) -> 10
    :param x int:
    :param y int:
    :return int:
    """
    if y == 0:
        return x
    return gcd_euclidian(x=y, y=x % y)


def gcd_lineal(x: int, y: int) -> int:
    """
    Return greatest common divisor of both elements.
    Time complexity is O(N) where N is min(x, y).
    Memory complexity is O(1).
    Example of usages:
    a = 10
    b = 20
    gcd_lineal(a, b) -> 10
    :param x int:
    :param y int:
    :return int:
    """
    if x == 0 or y == 0:
        return max(x, y)
    for i in range(min(x, y), -1, -1):
        if x % i == 0 and y % i == 0:
            return i
