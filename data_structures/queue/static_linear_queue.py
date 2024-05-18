from data_structures.linked_list.double_linked_list import DoubleLinkedList
from data_structures.array.static_multi_type_array import StaticMultiTypeArray


class StaticLinearQueue:
    """
    Implementation of Static Linear Queue.
    Under hood queue use Static Multi Type Array.
    For more information about available methods call all_methods() method.
    :param capacity - int optional, by default sets to 10. Size of capacity storage in queue.
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
    slq = StaticLinearQueue() # Definition of class
    slq.all_methods() -> list[str, str, ...] # all available methods.
    """
    def __init__(self, capacity: int = 10):
        self.queue = StaticMultiTypeArray(capacity=capacity)

    def dequeue(self, x: any) -> None:
        """
        Insert given object to the rear(end) of queue.
        Raise exception if queue is full(have maximum size of capacity).
        Time complexity is O(1).
        Example of Usages:
        slq = StaticLinearQueue()
        slq.dequeue(1) -> None
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
        slq = StaticLinearQueue()
        slq.dequeue(1) -> None
        slq.enqueue() -> 1
        :return object from the front(start) of queue:
        """
        if self.is_empty():
            raise IndexError("Can't delete from empty Queue")
        return self.queue.pop(0)

    def peek(self) -> object:
        """
        Return object from the front(start/head) of queue and not delete them.
        Raise exception if queue is empty.
        Time complexity O(1).
        Example of Usages:
        slq = StaticLinearQueue()
        slq.dequeue(1) -> None
        slq.peek() -> 1
        :return:
        """
        if self.is_empty():
            raise IndexError("Can't peek from empty Queue")
        return self.queue[0]

    def is_empty(self) -> bool:
        """
        Return True if queue is empty and otherwise return False.
        Time complexity O(1).
        Example of Usages:
        slq = StaticLinearQueue()
        slq.is_empty() -> True
        :return boolean true of false:
        """
        return self.queue.is_empty()

    def is_full(self) -> bool:
        """
        Return True if queue is full(have same size as capacity), otherwise return False.
        Time complexity O(1).
        Example of usages:
        slq = StaticLinearQueue(1)
        slq.dequeue(1)
        slq.is_full() -> True
        :return boolean true of false:
        """
        return self.queue.length() == self.queue.capacity

    def size(self) -> int:
        """
        Return actual size of queue.
        Time complexity O(1).
        Example of Usages:
        slq = StaticLinearQueue()
        slq.size() -> 0
        :return integer:
        """
        return self.queue.length()

    def __str__(self) -> str:
        """
        Return string representation of queue in the next format: Front<-|i0<-|i1<-|...<-|in-1<-|in<-|Rear.
        If queue is empty return string None.
        Time complexity O(N).
        Example of Usages:
        slq = StaticLinearQueue()
        for i in range(5):
            slq.dequeue(i)
        print(slq) -> Front<-|0<-|1<-|2<-|3<-|4<-|Rear
        :return string:
        """
        if self.is_empty():
            return 'None'
        output: StaticMultiTypeArray = StaticMultiTypeArray(capacity=self.queue.capacity + 3)
        output.append('Front')
        for item in self.queue:
            output.append(item)
        output.append('Rear')
        return '<-|'.join(f"'{item}'" if isinstance(item, str) else str(item) for item in output)

    def all_methods(self) -> list[str]:
        """
        Return list string names of all available methods in Queue.
        Example of Usages:
        slq = StaticLinearQueue()
        slq.all_methods() -> list[str, str, ...]
        :return list of strings:
        """
        return dir(StaticLinearQueue)
