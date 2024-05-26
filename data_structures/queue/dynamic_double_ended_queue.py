from data_structures.linked_list.double_linked_list import DoubleLinkedList
from data_structures.array.dynamic_multi_type_array import DynamicMultiTypeArray


class DynamicDoubleEndedQueue:
    """
    Implementation of Dynamic Double Ended Queue.
    Under hood queue use Double Linked List.
    For more information about available methods call all_methods() method.
    Definition of Linear Deque:
    Deque or Double Ended Queue is a generalized version of Queue
    data structure that allows insert and delete at both ends.
    Also, the problems where elements need to be removed and
    or added to both ends can be efficiently solved using Deque.
    Example of Usages:
    ddeq = DynamicDoubleEndedQueue() # Definition of class
    ddeq.all_methods() -> list[str, str, ...] # all available methods.
    """
    def __init__(self):
        self.dequeue = DoubleLinkedList()

    def push_back(self, x: any) -> None:
        """
        Insert given object to the rear(end) of deque.
        Time complexity is O(1).
        Example of Usages:
        ddeq = DynamicDoubleEndedQueue()
        ddeq.push_back(1) -> None
        :param x object any type:
        :return None:
        """
        self.dequeue.append(x)

    def push_right(self, x: any) -> None:
        """
        Insert given object to the front(start) of deque.
        Time complexity is O(1).
        Example of Usages:
        ddeq = DynamicDoubleEndedQueue()
        ddeq.push_right(1) -> None
        :param x object any type:
        :return None:
        """
        self.push_back(x)

    def push_front(self, x: any) -> None:
        """
        Insert given object to the front(start) of deque.
        Time complexity is O(1).
        Example of Usages:
        ddeq = DynamicDoubleEndedQueue()
        ddeq.push_front(1) -> None
        :param x object any type:
        :return None:
        """
        self.dequeue.prepend(x)

    def push_left(self, x: any) -> None:
        """
        Insert given object to the rear(end) of deque.
        Time complexity is O(1).
        Example of Usages:
        ddeq = DynamicDoubleEndedQueue()
        ddeq.push_left(1) -> None
        :param x object any type:
        :return None:
        """
        self.push_front(x)

    def extend_left(self, sequence: iter) -> None:
        """
        Adding all elements from given sequence to the front(start/left/head) of deque.
        Time complexity O(M) where M is length of sequence.
        Example of usage:
        ddeq = DynamicDoubleEndedQueue()
        ddeq.extend_left([1, 2, 3, 4, 5])
        print(ddeq) -> 'Front'<-|5<-|4<-|3<-|2<-|1<-|'Rear'
        :param sequence: iterable sequence
        :return: None
        """
        for item in sequence:
            self.push_front(item)

    def extend_front(self, sequence: iter) -> None:
        """
        Adding all elements from given sequence to the front(start/left/head) of deque.
        Time complexity O(M) where M is length of sequence.
        Example of usage:
        ddeq = DynamicDoubleEndedQueue()
        ddeq.extend_front([1, 2, 3, 4, 5])
        print(ddeq) -> 'Front'<-|5<-|4<-|3<-|2<-|1<-|'Rear'
        :param sequence: iterable sequence
        :return: None
        """
        self.extend_left(sequence)

    def extend_right(self, sequence: iter) -> None:
        """
        Adding all elements from given sequence to the back(end/right/tail) of deque.
        Time complexity O(M) where M is length of sequence.
        Example of usage:
        ddeq = DynamicDoubleEndedQueue()
        ddeq.extend_right([1, 2, 3, 4, 5])
        print(ddeq) -> 'Front'<-|1<-|2<-|3<-|4<-|5<-|'Rear'
        :param sequence: iterable sequence
        :return: None
        """
        for item in sequence:
            self.push_back(item)

    def extend_back(self, sequence: iter) -> None:
        """
        Adding all elements from given sequence to the back(end/right/tail) of deque.
        Time complexity O(M) where M is length of sequence.
        Example of usage:
        ddeq = DynamicDoubleEndedQueue()
        ddeq.extend_back([1, 2, 3, 4, 5])
        print(ddeq) -> 'Front'<-|1<-|2<-|3<-|4<-|5<-|'Rear'
        :param sequence: iterable sequence
        :return: None
        """
        self.extend_right(sequence)

    def pop_front(self) -> object:
        """
        Delete and return object from the front(start/head/left) of deque.
        Raise exception is deque is empty.
        Time complexity O(1).
        Example of Usages:
        ddeq = DynamicDoubleEndedQueue()
        ddeq.push_back(1) -> None
        ddeq.pop_front() -> 1
        :return object from the front(start) of deque:
        """
        if self.is_empty():
            raise IndexError("Can't delete from empty Deque")
        return self.dequeue.popleft()

    def pop_left(self) -> object:
        """
        Delete and return object from the front(start/head/left) of deque.
        Raise exception is deque is empty.
        Time complexity O(1).
        Example of Usages:
        ddeq = DynamicDoubleEndedQueue()
        ddeq.push_back(1) -> None
        ddeq.pop_left() -> 1
        :return object from the front(start) of deque:
        """
        return self.pop_front()

    def pop_back(self) -> object:
        """
        Delete and return object from the back(end/tail/right) of deque.
        Raise exception is deque is empty.
        Time complexity O(1).
        Example of Usages:
        ddeq = DynamicDoubleEndedQueue()
        ddeq.push_back(1) -> None
        ddeq.pop_back() -> 1
        :return object from the front(start) of deque:
        """
        if self.is_empty():
            raise IndexError("Can't delete from empty Deque")
        return self.dequeue.pop()

    def pop_right(self) -> object:
        """
        Delete and return object from the back(end/tail/right) of deque.
        Raise exception is deque is empty.
        Time complexity O(1).
        Example of Usages:
        ddeq = DynamicDoubleEndedQueue()
        ddeq.push_back(1) -> None
        ddeq.pop_right() -> 1
        :return object from the front(start) of deque:
        """
        return self.pop_back()

    def peek_left(self) -> object:
        """
        Return object from the front(start/head) of deque and not delete them.
        Raise exception if queue is empty.
        Time complexity O(1).
        Example of Usages:
        ddeq = DynamicDoubleEndedQueue()
        ddeq.push_back(1) -> None
        ddeq.peek_left() -> 1
        :return:
        """
        if self.is_empty():
            raise IndexError("Can't peek from empty Deque")
        return self.dequeue.head.data

    def peek_front(self) -> object:
        """
        Return object from the front(start/head) of deque and not delete them.
        Raise exception if queue is empty.
        Time complexity O(1).
        Example of Usages:
        ddeq = DynamicDoubleEndedQueue()
        ddeq.push_back(1) -> None
        ddeq.peek_front() -> 1
        :return:
        """
        return self.peek_left()

    def peek_right(self) -> object:
        """
        Return object from the rear(end/tail/right) of deque and not delete them.
        Raise exception if queue is empty.
        Time complexity O(1).
        Example of Usages:
        ddeq = DynamicDoubleEndedQueue()
        ddeq.push_back(1) -> None
        ddeq.peek_right() -> 1
        :return:
        """
        if self.is_empty():
            raise IndexError("Can't peek from empty Deque")
        return self.dequeue.tail.data

    def peek_back(self) -> object:
        """
        Return object from the rear(end/tail/right) of deque and not delete them.
        Raise exception if queue is empty.
        Time complexity O(1).
        Example of Usages:
        ddeq = DynamicDoubleEndedQueue()
        ddeq.push_back(1) -> None
        ddeq.peek_back() -> 1
        :return:
        """
        return self.peek_right()

    def is_empty(self) -> bool:
        """
        Return True if deque is empty and otherwise return False.
        Time complexity O(1).
        Example of Usages:
        ddeq = DynamicDoubleEndedQueue()
        ddeq.is_empty() -> True
        :return boolean true of false:
        """
        return self.dequeue.is_empty()

    def size(self) -> int:
        """
        Return actual size of deque.
        Time complexity O(1).
        Example of Usages:
        ddeq = DynamicDoubleEndedQueue()
        ddeq.size() -> 0
        :return integer:
        """
        return self.dequeue.length()

    def __str__(self) -> str:
        """
        Return string representation of deque in the next format: Front<-|i0<-|i1<-|...<-|in-1<-|in<-|Rear.
        If deque is empty return string None.
        Time complexity O(N).
        Example of Usages:
        ddeq = DynamicDoubleEndedQueue()
        for i in range(5):
            ddeq.push_back(i)
        print(ddeq) -> Front<-|0<-|1<-|2<-|3<-|4<-|Rear
        :return string:
        """
        if self.is_empty():
            return 'None'
        output: DynamicMultiTypeArray = DynamicMultiTypeArray()
        output.append('Front')
        item = self.dequeue.head
        while item:
            output.append(item.data)
            item = item.next
        output.append('Rear')
        return '<-|'.join(f"'{item}'" if isinstance(item, str) else str(item) for item in output)

    def clear(self) -> None:
        """
        Clear deque(delete all elements from deque).
        Time complexity O(1).
        Example of usages:
        ddeq = DynamicDoubleEndedQueue()
        ddeq.clear()
        :return: None
        """
        self.dequeue.clear()

    def all_methods(self) -> list[str]:
        """
        Return list string names of all available methods in Deque.
        Example of Usages:
        ddeq = DynamicDoubleEndedQueue()
        ddeq.all_methods() -> list[str, str, ...]
        :return list of strings:
        """
        return dir(DynamicDoubleEndedQueue)
