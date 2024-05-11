def binary_search_leftmost(sequence: iter, target: any, possibly: bool = False) -> int:
    """
    Return leftmost index of all occurrences target in sequence if it exists, otherwise return -1*.
    Target should support comparison between all elements in sequence, otherwise function throw an exception.
    Time complexity is O(log(N)) where N is length of sequence.
    Memory complexity is O(1).
    *- if param "possibly" is False(by default), otherwise read more below about "possibly" param.
    :param sequence - sorted sequence in increasing order with existing dunder __getitem__ and __len__ methods:
    :param target - any object that will be search:
    :param possibly - optional boolean, by default sets to False. If True return index of element that may be of given target if target not exists in sequence,
    otherwise if it set to False return -1 if target doesn't exist in sequence.
    :return int:
    Example us usages:
    seq: list[int] = [1, 2, 2, 3, 4, 5]
    binary_search_leftmost(seq, 2) -> 1
    binary_search_leftmost(seq, 6) -> -1
    seq: str = 'aabbcdefg'
    binary_search_leftmost(seq, 'a') -> 0
    binary_search_leftmost(seq, 'z', possibly=True) -> 9
    """
    n: int = len(sequence)
    left: int = 0
    right: int = n - 1
    seen: bool = False
    while left <= right:
        middle: int = (left + right) >> 1
        if sequence[middle] >= target:
            if sequence[middle] == target:
                seen = True
            right = middle - 1
        else:
            left = middle + 1
    if possibly:
        return right + 1
    return -1 if not seen else right + 1
