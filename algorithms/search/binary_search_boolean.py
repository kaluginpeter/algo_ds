def binary_search_boolean(sequence: iter, target: any) -> bool:
    """
    Return True if target exist in sequence, otherwise return False.
    Target should support comparison between all elements in sequence, otherwise function throw an exception.
    Time complexity is O(log(N)) where N is length of sequence.
    Memory complexity is O(1).
    :param sequence - sorted sequence in increasing order with existing dunder __getitem__ and __len__ methods:
    :param target - any object that will be search:
    :return boolean true of false:
    Example us usages:
    seq: list[int] = [1, 2, 3, 4, 5]
    binary_search_boolean(seq, 1) -> True
    binary_search_boolean(seq, 6) -> False
    seq: str = 'abcdefg'
    binary_search_boolean(seq, 'a') -> True
    binary_search_boolean(seq, 'z') -> False
    """
    left, right = 0, len(sequence) - 1
    while left <= right:
        middle: int = (left + right) >> 1
        if sequence[middle] == target:
            return True
        elif sequence[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return False
