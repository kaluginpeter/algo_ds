from data_structures.array.dynamic_multi_type_array import DynamicMultiTypeArray


class MinimumHeap:
    """
    Minimum Heap - A Min-Heap is defined as a type of Heap Data Structure
    in which each node is smaller than or equal to its children.
    The heap data structure is a type of binary tree that is commonly used
    in computer science for various purposes, including sorting, searching, and organizing data.
    Example of Usages:
    h = MinimumHeap()
    h.all_methods() -> list[str]
    """
    def __init__(self) -> None:
        self.heap = DynamicMultiTypeArray()
        self.heap.append(0)

    def push(self, item) -> None:
        """
        Push given item in heap.
        Time Complexity O(logN).
        Example of usages:
        h = MinimumHeap()
        h.push(1) -> None
        print(h) -> [1]
        :param item: any object than can be compared with other previous objects in heap.
        :return: None
        """
        self.heap.append(item)
        current_index: int = self.heap.length() - 1
        parent: int = current_index >> 1

        while parent > 0 and self.heap[parent] > self.heap[current_index]:
            self.heap[parent], self.heap[current_index] = self.heap[current_index], self.heap[parent]
            current_index, parent = parent, parent >> 1

    def __swapper(self, current_index: int) -> None:
        """
        Make swap and balance current heap with given index
        :param current_index: Index of current item that needs to swap in heap to balance.
        :return: None
        """
        upper_bound: int = self.heap.length()
        while 2 * current_index < upper_bound:
            if (
                2 * current_index + 1 < upper_bound
                and self.heap[2 * current_index] > self.heap[2 * current_index + 1]
                and self.heap[current_index] > self.heap[2 * current_index + 1]
            ):
                self.heap[current_index], self.heap[2 * current_index + 1] = (
                    self.heap[2 * current_index + 1], self.heap[current_index]
                )
                current_index = 2 * current_index + 1
            elif self.heap[current_index] > self.heap[2 * current_index]:
                self.heap[current_index], self.heap[2 * current_index] = (
                    self.heap[2 * current_index], self.heap[current_index]
                )
                current_index *= 2
            else: break

    def peek(self) -> object:
        """
        Return top of the heap and not delete him if heap is not empty, otherwise raise error.
        Time Complexity O(1).
        Example of Usages:
        h = MinimumHeap()
        h.push(0) -> None
        h.peek() -> 0
        :return: object, top of the heap.
        """
        if self.heap.length() == 1:
            raise IndexError("Can't peek from empty heap!")
        return self.heap[1]

    def pop(self) -> object:
        """
        Return element from the top of heap and delete then.
        If heap is empty raise error.
        Time Complexity O(logN).
        Example of Usages:
        h = MinimumHeap()
        h.push(1) -> None
        h.pop() -> 1
        print(h) -> []
        :return: element from the top of heap.
        """
        if self.heap.length() == 1:
            raise IndexError("Can't pop from empty heap!")
        elif self.heap.length() == 2:
            return self.heap.pop()

        top = self.heap[1]

        self.heap[1] = self.heap.pop()
        current_index: int = 1
        self.__swapper(current_index)

        return top

    def heapify(self, sequence: iter) -> None:
        """
        Make heap from the given sequence.
        If heap have some data before calling function,
        after ".heapify(*args)" method heap will have new data from given sequence.
        Time Complexity O(N).
        Example of Usages:
        h = MinimumHeap()
        h.heapify([3, 2, -1, 1, 0, 4, -3]) -> None
        print(h) -> [-3, 0, -1, 1, 2, 4, 3]
        :param sequence: iterable sequence with __getitem__ dunder methods
        :return: -> None
        """
        self.heap.clear()
        self.heap.append(0)
        for item in sequence: self.push(item)

        current_index: int = (self.heap.length() - 1) >> 1
        while current_index > 0:
            self.__swapper(current_index)
            current_index -= 1

    def __str__(self) -> str:
        """
        Return string representation of heap.
        If heap is empty return "[]".
        Example of Usages:
        h = MinimumHeap()
        h.push(1) -> None
        print(h) -> [1]
        :return: string representation of heap
        """
        if self.heap.length() == 1:
            return '[]'
        output: str = ', '.join(f"'{item}'" if isinstance(item, str) else str(item) for item in self.heap)
        return '[' + output[3:] + ']'

    def all_methods(self) -> list[str]:
        """
        Return list names(string) of all methods existing in class.
        :return: list of string representing name of all available methods in class.
        """
        return dir(MinimumHeap)
