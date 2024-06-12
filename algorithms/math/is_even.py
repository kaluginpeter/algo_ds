def is_even(number: int) -> bool:
    """
    Function that check if given number is even,
    if it is, function return True, otherwise return False.
    Time Complexity O(1).
    Memory Complexity O(1).
    Example of usages:
    is_even(5) -> False
    is_even(6) -> True
    :param number: Negative or Positive integer, if it not instances of "int" type,
        function will throw an exception.
    :return: boolean type True of False.
    """
    return [False, True][~(number & 1)]