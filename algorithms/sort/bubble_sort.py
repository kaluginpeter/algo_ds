def bubble_sort(sequence: iter, reverse: bool = False) -> None:
    """
    Function thats make bubble sort in given sequence.
    Time Complexity O(N**2), but optimized(amortized) in some cases to O(N).
    Memory Complexity O(1).
    Example of Usages:
    l = [1, 3, 5, 2, 4]
    bubble_sort(l) -> None
    print(l) -> [1, 2, 3, 4, 5]
    :param sequence: Iterable sequence that have __getitem__ and __le__ dunder methods.
    :param reverse: boolean, optional, by default sets to False.
        If False, sorting in ascending order(i0 <= i1 <= ... <= in-1 <= in).
        Otherwise if True, sorting in descending order(i0 >= i1 >= ... >= in-1 >= in).
    :return:
    """
    for right in range(1, len(sequence)):
        sorted_state: bool = True
        for left in range(len(sequence) - right):
            if (
                sequence[left] > sequence[left + 1] if not reverse
                else sequence[left] < sequence[left + 1]
            ):
                sorted_state = False
                sequence[left], sequence[left + 1] = sequence[left + 1], sequence[left]
        if sorted_state: break