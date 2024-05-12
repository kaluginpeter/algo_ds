def lineal_search_bool(sequence: iter, target: any) -> bool:
    """
    Return True if target exist in sequence, otherwise return False.
    Target should support comparison between all elements in sequence, otherwise function throw an exception.
    Time complexity is O(N) where N is length of sequence.
    Memory complexity is O(1).
    :param sequence - sequence in any order with existing dunder __iter__ and __eq__ methods:
    :param target - any object that will be search:
    :return boolean true of false:
    Example us usages:
    seq: list[int] = [1, 2, 3, 4, 5]
    lineal_search_bool(seq, 1) -> True
    lineal_search_bool(seq, 6) -> False
    seq: str = 'abcdefg'
    lineal_search_bool(seq, 'a') -> True
    lineal_search_bool(seq, 'z') -> False
    """
    for i in sequence:
        if i == target:
            return True
    return False
