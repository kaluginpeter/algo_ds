from data_structures.linked_list.double_linked_list import DoubleLinkedList
from data_structures.array.dynamic_multi_type_array import DynamicMultiTypeArray


class DynamicLinearQueue:
    """
    Implementation of Dynamic Linear Queue.
    Under hood queue use Double Linked List.
    For more information about available methods call all_methods() method.
    Definition of Linear Queue:
    A linear queue is a type of data structure where the data elements are arranged in a sequential manner,
    and the addition of new elements is done from one end and the deletion of elements is performed from the other end.
    It follows the FIFO (First In First Out) principle.
    An example of a linear queue is a queue of customers waiting in a line to pay for their groceries at a supermarket.
    The first customer to arrive at the checkout line is the first customer to be served,
    and the last customer to arrive will be the last to be served. If a new customer arrives,
    they must stand at the end of the queue,
    and the customer at the front of the queue will be serviced and removed from the queue first.
    This process will continue until all the customers in the queue have been served.
    Example of Usages:
    dlq = DynamicLinearQueue() # Definition of class
    dlq.all_methods() -> list[str, str, ...] # all available methods.
    """
    def __init__(self):
        self.queue = DoubleLinkedList()

    def dequeue(self, x: any) -> None:
        """
        Insert given object to the rear(end) of queue.
        Time complexity is O(1).
        Example of Usages:
        dlq = DynamicLinearQueue()
        dlq.dequeue(1) -> None
        :param x object any type:
        :return None:
        """
        self.queue.append(x)

    def enqueue(self) -> object:
        """
        Delete and return object from the front(start/head) of queue.
        Raise exception is queue is empty.
        Time complexity O(1).
        Example of Usages:
        dlq = DynamicLinearQueue()
        dlq.dequeue(1) -> None
        dlq.enqueue() -> 1
        :return object from the front(start) of queue:
        """
        if self.is_empty():
            raise IndexError("Can't delete from empty Queue")
        return self.queue.popleft()

    def peek(self) -> object:
        """
        Return object from the front(start/head) of queue and not delete them.
        Raise exception if queue is empty.
        Time complexity O(1).
        Example of Usages:
        dlq = DynamicLinearQueue()
        dlq.dequeue(1) -> None
        dlq.peek() -> 1
        :return:
        """
        if self.is_empty():
            raise IndexError("Can't peek from empty Queue")
        return self.queue.head.data

    def is_empty(self) -> bool:
        """
        Return True if queue is empty and otherwise return False.
        Time complexity O(1).
        Example of Usages:
        dlq = DynamicLinearQueue()
        dlq.is_empty() -> True
        :return boolean true of false:
        """
        return self.queue.is_empty()

    def size(self) -> int:
        """
        Return actual size of queue.
        Time complexity O(1).
        Example of Usages:
        dlq = DynamicLinearQueue()
        dlq.size() -> 0
        :return integer:
        """
        return self.queue.length()

    def __str__(self) -> str:
        """
        Return string representation of queue in the next format: Front<-|i0<-|i1<-|...<-|in-1<-|in<-|Rear.
        If queue is empty return string None.
        Time complexity O(N).
        Example of Usages:
        dlq = DynamicLinearQueue()
        for i in range(5):
            dlq.dequeue(i)
        print(dlq) -> Front<-|0<-|1<-|2<-|3<-|4<-|Rear
        :return string:
        """
        if self.is_empty():
            return 'None'
        output: DynamicMultiTypeArray = DynamicMultiTypeArray()
        output.append('Front')
        item = self.queue.head
        while item:
            output.append(item.data)
            item = item.next
        output.append('Rear')
        return '<-|'.join(f"'{item}'" if isinstance(item, str) else str(item) for item in output)

    def all_methods(self) -> list[str]:
        """
        Return list string names of all available methods in Queue.
        Example of Usages:
        dlq = DynamicLinearQueue()
        dlq.all_methods() -> list[str, str, ...]
        :return list of strings:
        """
        return dir(DynamicLinearQueue)
