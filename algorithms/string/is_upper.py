def is_upper(string: str) -> bool:
    """
    Function that return if all alphabetical characters in string have upper case,
    if it is, function return True, otherwise return False.
    Time complexity O(N).
    Memory Complexity O(1).
    Example of Usages:
    is_upper('S1') -> True
    is_upper('hello') -> False
    :param string: object of string instance.
    :return: boolean True of False.
    """
    alphabetical_chars: bool = False
    for character in string:
        if character.isalpha():
            alphabetical_chars = True
            if character != character.upper():
                return False
    return alphabetical_chars
