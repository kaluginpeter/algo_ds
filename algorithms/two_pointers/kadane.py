def kadane_two_pointers(sequence: iter) -> int | float:
    """
    Functions that takes sequence of numbers(positive or negative),
    and return maximum subarray sum.
    If sequence if empty, functions return "0" as integer.
    Time Complexity O(N).
    Memory Complexity O(1).
    Example of usages:
    s1 = [1, 2, 3, 4, 5]
    s2 = (4, -2, 3, -7, 5)
    s3 = [1, -2, 1]
    kadane_two_pointers(s1) -> 15
    kadane_two_pointers(s2) -> 5
    kadane_two_pointers(s3) -> 1
    : sequence - sequence of numbers(int or float)
    : output - maximum subarray sum
    """
    maximum_sum: int = float('-inf')
    current_sum: int = 0
    for number in sequence:
        current_sum = max(current_sum + number, number)
        maximum_sum = max(maximum_sum, current_sum)
    if maximum_sum == float('-inf'):
        return 0
    return maximum_sum


def kadane_sliding_window(sequence: iter) -> tuple[int, int]:
    """
    Functions that takes sequence of numbers(positive or negative),
    and return first maximum subarray sum indexes from start to end inclusive.
    If sequence if empty, functions return (-1, -1).
    Note: function works in 0 indexed notation.
    Time Complexity O(N).
    Memory Complexity O(1).
    Example of usages:
    s1 = [1, 2, 3, 4, 5]
    s2 = (4, -2, 3, -7, 5)
    s3 = [1, -2, 1]
    kadane_sliding_window(s1) -> (0, 4)
    kadane_sliding_window(s2) -> (0, 2)
    kadane_sliding_window(s3) -> (0, 0)
    : sequence - sequence of numbers(int or float)
    : output - maximum subarray sum indexes, (left, right*)
    *inclusive
    """
    max_left: int = -1
    max_right: int = -1
    maximum_sum: int = float('-inf')
    current_sum: int = 0
    left: int = 0
    for right in range(len(sequence)):
        if current_sum < 0:
            current_sum = 0
            left = right
        current_sum += sequence[right]
        if current_sum > maximum_sum:
            max_left, max_right = left, right
            maximum_sum = current_sum
    if maximum_sum == float('-inf'):
        return (-1, -1)
    return (max_left, max_right)
