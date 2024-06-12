def is_digit(string: str) -> bool:
    """
    Function that check if all characters in string are digit(base 10),
    if it is, function return True, otherwise return False.
    Time Complexity O(N).
    Memory Complexity O(1).
    Example of Usages:
    is_digit('123434324344') -> True
    is_digit('123o456798a') -> False
    :param string: object instance of string, if it not that,
        function will throw an exception.
    :return: boolean True of False.
    """
    digits: set[int] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    for character in string:
        if character not in digits:
            return False
    return True
