def quick_sort(sequence: iter, reverse: bool = False) -> None:
    """
    Function that make quick sort wight randomized pivot element.
    Time Complexity: Most average O(Nlogn), but in the worst case O(N**2)
    Memory Complexity: O(1).
    Not stable.
    Example of Usages:
    l = [1, 3, 2, 5, 4]
    quick_sort(l) -> None
    print(l) -> [1, 2, 3, 4, 5]
    :param sequence: Iterable sequence that have __getitem__ and __le__ dunder methods.
    :param reverse: boolean, optional, by default sets to False.
        If False, sorting sequence in ascending order(i0 <= i1 <= ... <= in-1 <= in).
        Otherwise if True, sorting sequence in descending order(i0 >= i1 >= ... >= in-1 >= in).
    :return:
    """
    from random import randint
    def _quick_sort(sequence: iter, start: int = 0, end: int = 0) -> None:
        if end - start + 1 <= 1: return sequence
        pivot_index: int = randint(start, end)
        sequence[end], sequence[pivot_index] = sequence[pivot_index], sequence[end]
        left = start
        for item in range(start, end):
            if (
                sequence[item] < sequence[end] if not reverse
                else sequence[item] > sequence[end]
            ):
                sequence[item], sequence[left] = sequence[left], sequence[item]
                left += 1
        sequence[end], sequence[left] = sequence[left], sequence[end]
        _quick_sort(sequence, start, left - 1)
        _quick_sort(sequence, left + 1, end)

    _quick_sort(sequence, 0, len(sequence) - 1)
