def merge_sort(sequence: iter, reverse: bool = False) -> list:
    """
    Function that making merge sort from given sequence.
    Stable sort.
    Time Complexity O(NlogN).
    Memory Complexity O(N).
    Example of usages:
    l = [1, 3, 2, 5, 4]
    merge_sort(l) -> [1, 2, 3, 4, 5]
    :param sequence: Sequence that have __getitem__ and __le__ dunder methods.
    :param reverse: Boolean, optional, by default sets to False.
        If True, sorting sequence in descending order (i0 >= i1 >= ... >= in-1 >= in).
        Otherwise if False, sorting sequence in ascending order(i0 <= i1 <= ... <= in-1 <= in).
    :return:
    """
    len_of_sequence: int = len(sequence)
    if len_of_sequence <= 1:
        return sequence

    middle: int = len_of_sequence >> 1
    left: iter = merge_sort(sequence[:middle], reverse=reverse)
    right: iter = merge_sort(sequence[middle:], reverse=reverse)
    output: list = list()
    left_idx = right_idx = 0
    left_len, right_len = len(left), len(right)
    while left_idx < left_len and right_idx < right_len:
        if (
                left[left_idx] <= right[right_idx] if not reverse
                else left[left_idx] > right[right_idx]
        ):
            output.append(left[left_idx])
            left_idx += 1
        else:
            output.append(right[right_idx])
            right_idx += 1
    return output + left[left_idx:] + right[right_idx:]
