from data_structures.arrays.static_multi_type_array import StaticMultiTypeArray
from algorithms.search.binary_search_leftmost import binary_search_leftmost


class BinaryMonotonicIncreasingStaticStack:
    """
    Implementation of Binary Monotonic Increasing Static Stack data structure.
    The binary monotonously increasing stack uses the leftmost binary search in the push method, thereby
    providing an "always" increasing stack and the ability not to delete elements, as in a simple monotonous increasing stack.
    Binary Monotonic Increasing Static Stack using Static Multi Type Array for storing objects.
    Binary Monotonic Increasing Static Stack (can store only one of the different data types, because
    implementation use some amortized operation and attempting to push
    some different types of object will throw an exception)*.
    * - only if min_value_method or max_value_method is True
    Required params:
    min_value_method: bool optional, by default sets to false. If true keep track minimum value in stack
    max_value_method: bool optional, by default sets to false. It true keep track maximum value in stack
    Example of usages:
    bmiss = BinaryMonotonicIncreasingStaticStack()
    For more information about available methods use all_methods() methods, like:
    bmiss.all_methods()
    """
    def __init__(self, capacity: int = 10, min_value_method: bool = False, max_value_method: bool = False):
        self.stack: StaticMultiTypeArray = StaticMultiTypeArray(capacity=capacity)
        self.min_value_method = min_value_method
        self.max_value_method = max_value_method

    def __str__(self) -> str:
        """
        Return string representation of stack.
        Use for python builtin function str().
        Example of usages:
        bmiss = BinaryMonotonicIncreasingStaticStack()
        str(bmiss)
        :return string representation of stack:
        """
        if self.is_empty():
            return '[]'
        output: StaticMultiTypeArray = StaticMultiTypeArray(capacity=self.length())
        for i in self.stack:
            output.append(i)
        return '[' + ', '.join(f"'{item}'" if type(item) == str else str(item) for item in output) + ']'

    def push(self, x: any) -> None:
        """
        Push element to the top of stack.
        Be careful in usage when attempting push object with different data type,
        stack use amortized min_value method, so pushing will throw exception during comparison elements.
        Time complexity is O(log(N)) where N is a length of stack.
        Example of usages:
        bmiss = BinaryMonotonicIncreasingStaticStack()
        bmiss.push(1)
        :param x:
        :return None:
        """
        if self.is_empty():
            self.stack.append(x)
            return

        if (self.min_value_method or self.max_value_method) and not isinstance(x, type(self.peek())):
            raise TypeError("Can't append element not the same type as other in stack")

        idx: int = binary_search_leftmost(self.stack, x, possibly=True)
        self.stack.insert(idx, x)

    def pop(self) -> object:
        """
        Pop element from the top of stack and return it.
        Raise error if stack is empty.
        Time complexity is O(1).
        Example of usages:
        bmiss = BinaryMonotonicIncreasingStaticStack()
        bmiss.push(1)
        bmiss.pop()
        :return object(popped element):
        """
        return self.stack.pop()

    def peek(self) -> object:
        """
        Return last(from the top) element from the stack.
        Raise error if stack is empty.
        Time complexity is O(1)
        Example of usages:
        bmiss = BinaryMonotonicIncreasingStaticStack()
        bmiss.push(1)
        bmiss.peek()
        :return object(element in stack):
        """
        if self.is_empty():
            raise IndexError("Can't peek from empty stack")
        return self.stack[-1]

    def min_value(self) -> object:
        """
        Return minimum element in stack. Raise error if stack is empty.
        Be careful in usage, because if you store some different types in stack,
        method will throw exception during comparison between them.
        Time complexity amortized, so its O(1).
        Example of usages:
        bmiss = BinaryMonotonicIncreasingStaticStack()
        bmiss.push(1)
        bmiss.min_value()
        :return object(element in stack):
        """
        if not self.min_value_method:
            raise SystemError("Method not available! Set boolean min_value_method on True")
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[0]

    def max_value(self) -> object:
        """
        Return maximum element in stack. Raise error if stack is empty.
        Be careful in usage, because if you store some different types in stack,
        method will throw exception during comparison between them.
        Time complexity amortized, so its O(1).
        Example of usages:
        bmiss = BinaryMonotonicIncreasingStaticStack()
        bmiss.push(1)
        bmiss.max_value()
        :return object(element in stack):
        """
        if not self.max_value_method:
            raise SystemError("Method not available! Set boolean max_value_method on True")
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.peek()

    def length(self) -> int:
        """
        Return integer represent size(all elements store in stack) of stack.
        Time complexity amortized, so its O(1).
        Example of usages:
        bmiss = BinaryMonotonicIncreasingStaticStack()
        bmiss.length()
        :return integer:
        """
        return self.stack.length()

    def is_empty(self) -> bool:
        """
        Return True if stack is empty, otherwise return False.
        Example of usages:
        bmiss = BinaryMonotonicIncreasingStaticStack()
        bmiss.is_empty()
        :return boolean true of false:
        """
        return self.stack.is_empty()

    def clear(self) -> None:
        """
        Clear all data in stack.
        Example of usages:
        bmiss = BinaryMonotonicIncreasingStaticStack()
        for i in range(5):
            bmiss.push(i)
        bmiss.clear()
        :return None:
        """
        self.stack.clear()

    def all_methods(self) -> list[str]:
        """
        Returning list names of all available methods.
        Example of usages:
        bmiss = BinaryMonotonicIncreasingStaticStack()
        bmiss.all_methods()
        :return list of strings:
        """
        return dir(BinaryMonotonicIncreasingStaticStack)