def is_odd(number: int) -> bool:
    """
    Function that check if number is odd,
    if it is, function return True, otherwise return False.
    Time Complexity O(1).
    Memory Complexity O(1).
    Example of usages:
    is_odd(8) -> False
    is_odd(3) -> True
    :param number: Negative or Positive integer, if it not instances of "int" type,
        function will throw an exception.
    :return: boolean type True of False.
    """
    return [False, True][number & 1]