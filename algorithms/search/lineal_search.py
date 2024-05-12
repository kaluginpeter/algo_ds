def lineal_search(sequence: iter, target: any) -> int:
    """
    Return leftmost index of all occurrences target in sequence if it exists, otherwise return -1.
    Target should support comparison between all elements in sequence, otherwise function throw an exception.
    Time complexity is O(N) where N is length of sequence.
    Memory complexity is O(1).
    :param sequence - sequence in any order with existing dunder __getitem__, __len__, __iter__, __eq__ methods:
    :param target - any object that will be search:
    :return int:
    Example us usages:
    seq: list[int] = [1, 2, 2, 3, 4, 5]
    lineal_search(seq, 2) -> 1
    lineal_search(seq, 6) -> -1
    seq: str = 'aabbcdefg'
    lineal_search(seq, 'a') -> 0
    lineal_search(seq, 'z') -> -1
    """
    for i in range(len(sequence)):
        if sequence[i] == target:
            return i
    return -1
