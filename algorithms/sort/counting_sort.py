def counting_sort(sequence: iter, reverse: bool = False) -> list[int]:
    """
    Make counting sort of given sequence.
    Time Complexity O(N).
    Memory Complexity O(N).
    Example of usages:
    l = [1, 3, 5, 2, 4]
    counting_sort(l) -> [1, 2, 3, 4, 5]
    :param sequence: Iterable sequence of integers(0 <= integer <= float)
    :param reverse: boolean, optional, by default sets to False.
        If True, sort sequence in descending order(i0 >= i1 >= ... >= in-1 >= in).
        Otherwise if False, sort sequence in ascending order(i0 <= i1 <= ... <= in-1 <= in).
    :return: sorted array of integers
    """
    upper_boundary: int = max(sequence)
    frequences: list[int] = [0 for _ in range(upper_boundary + 1)]
    for number in sequence:
        frequences[number] += 1
    output_list: list[int] = []
    if not reverse:
        for number in range(upper_boundary + 1):
            if frequences[number] > 0:
                output_list += [number] * frequences[number]
    elif reverse:
        for number in range(upper_boundary, -1, -1):
            if frequences[number] > 0:
                output_list += [number] * frequences[number]
    return output_list
