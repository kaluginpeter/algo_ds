def binary_search(sequence: iter, target: any) -> int:
    """
    Return index of any occurrences in sequence if it exists, otherwise return -1.
    Target should support comparison between all elements in sequence, otherwise function throw an exception.
    Time complexity is O(log(N)) where N is length of sequence.
    Memory complexity is O(1).
    :param sequence - sorted sequence in increasing order with existing dunder __getitem__ and __len__ methods:
    :param target - any object that will be search:
    :return int:
    Example us usages:
    seq: list[int] = [1, 2, 3, 4, 5]
    binary_search_boolean(seq, 1) -> 0
    binary_search_boolean(seq, 6) -> -1
    seq: str = 'abcdefg'
    binary_search_boolean(seq, 'a') -> 0
    binary_search_boolean(seq, 'z') -> -1
    """
    n: int = len(sequence)
    left: int = 0
    right: int = n - 1
    while left <= right:
        middle: int = (left + right) >> 1
        if sequence[middle] == target:
            return middle
        elif sequence[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return -1
