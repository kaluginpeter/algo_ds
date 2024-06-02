def selection_sort(sequence: iter, reverse: bool = False) -> None:
    """
    Function that making selection sort in given sequence.
    Stable sort.
    Time Complexity O(N**2).
    Memory Complexity O(1).
    Example of usages:
    l = [1, 3, 5, 2, 4]
    selection_sort(l) -> None
    print(l) -> [1, 2, 3, 4, 5]
    :param sequence: Sequence that have __getitem__ and __le__ methods.
    :param reverse: Boolean, optional, by default sets to False.
        If True sorting sequence in descending order (i0 >= i1 >= ... >= in-1 >= in).
        Otherwise sorting sequence in ascending order (i0 <= i1 <= ... <= in - 1 <= in).
    :return: None
    """
    for left in range(len(sequence)):
        smallest_element_idx = left
        for right in range(left + 1, len(sequence)):
            if (
                    (sequence[right] < sequence[smallest_element_idx]) if not reverse
                    else (sequence[right] > sequence[smallest_element_idx])
            ):
                smallest_element_idx = right
        sequence[left], sequence[smallest_element_idx] = sequence[smallest_element_idx], sequence[left]
