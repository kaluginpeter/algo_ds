def is_cycle(head) -> bool:
    """
    Return true if linked list have cycle, otherwise return false.
    Using Tortoise and Hare algorithm.
    Your Linked List should have .next attribute
    Time complexity O(N).
    Memory complexity O(1).
    Example of usages:
    from data_structures.linked_list.single_linked_list import SingleLinkedList
    from data_structures.linked_list.circular_linked_list import CircularLinkedList
    sl = SingleLinkedList()
    cl = CircularLinkedList()
    for i in range(10):
        sl.append(i)
        cl.append(i)
    is_cycle(sl.head) -> False
    is_cycle(cl.head) -> True
    :param head of linked list:
    :return boolean true of false:
    """
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
