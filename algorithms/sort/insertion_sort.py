def insertion_sort(sequence: iter, reverse: bool = False) -> None:
    """
    Function that making insertion sort in given sequence.
    Stable sort.
    Time Complexity O(N**2).
    Memory Complexity O(1).
    Example of usages:
    l = [1, 3, 4, 2, 5]
    insertion_sort(l) -> None
    print(l) -> [1, 2, 3 ,4 ,5]
    :param sequence: Sequence that gave __getitem__ and __le__ dunder methods.
    :param reverse: Boolean, optional, by default sets to False.
        If True, sorting sequence in descending order (i0 >= i1 >= ... >= in-1 >= in).
        Otherwise if False, sorting sequence in ascending order (i0 <= i1 <= ... <= in-1 <= in).
    :return: None
    """
    for right in range(1, len(sequence)):
        current_right = sequence[right]
        while (
                right > 0 and
                (
                        (sequence[right - 1] > current_right) if not reverse
                        else (sequence[right - 1] < current_right)
                )
        ):
            sequence[right] = sequence[right - 1]
            right -= 1
        sequence[right] = current_right
