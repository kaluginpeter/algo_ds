from data_structures.array.dynamic_multi_type_array import DynamicMultiTypeArray


class MonotonicDecreasingDynamicStack:
    """
    Implementation of Monotonic Decreasing Dynamic Stack data structure.
    Monotonic Decreasing Dynamic Stack using Dynamic Multi Type Array for storing objects.
    Monotonic Decreasing Dynamic Stack (can store only one of the different data types, because
    implementation use some amortized operation and attempting to push
    some different types of object will throw an exception)*.
    * - only if min_value_method or max_value_method is True
    Required params:
    min_value_method: bool optional, by default sets to false. If true keep track minimum value in stack
    max_value_method: bool optional, by default sets to false. It true keep track maximum value in stack
    Example of usages:
    mdds = MonotonicDecreasingDynamicStack()
    For more information about available methods use all_methods() methods, like:
    mdds.all_methods()
    """
    def __init__(self, min_value_method: bool = False, max_value_method: bool = False):
        self.stack: DynamicMultiTypeArray = DynamicMultiTypeArray()
        self.min_value_method = min_value_method
        self.max_value_method = max_value_method

    def __str__(self) -> str:
        """
        Return string representation of stack.
        Use for python builtin function str().
        Example of usages:
        mdds = MonotonicDecreasingDynamicStack()
        str(mdds)
        :return string representation of stack:
        """
        if self.is_empty():
            return '[]'
        output: DynamicMultiTypeArray = DynamicMultiTypeArray()
        for i in self.stack:
            output.append(i)
        return '[' + ', '.join(f"'{item}'" if type(item) == str else str(item) for item in output) + ']'

    def push(self, x: any) -> None:
        """
        Push element to the top of stack.
        Be careful in usage when attempting push object with different data type,
        stack use amortized min_value method, so pushing will throw exception during comparison elements.
        Time complexity is O(1).
        Example of usages:
        mdds = MonotonicDecreasingDynamicStack()
        mdds.push(1)
        :param x:
        :return None:
        """
        if self.is_empty():
            self.stack.append(x)
            return

        if (self.min_value_method or self.max_value_method) and not isinstance(x, type(self.peek())):
            raise TypeError("Can't append element not the same type as other in stack")

        while self.stack and self.peek() < x:
            self.pop()

        self.stack.append(x)

    def pop(self) -> object:
        """
        Pop element from the top of stack and return it.
        Raise error if stack is empty.
        Time complexity is O(1).
        Example of usages:
        mdds = MonotonicDecreasingDynamicStack()
        mdds.push(1)
        mdds.pop()
        :return object(popped element):
        """
        return self.stack.pop()

    def peek(self) -> object:
        """
        Return last(from the top) element from the stack.
        Raise error if stack is empty.
        Time complexity is O(1)
        Example of usages:
        mdds = MonotonicDecreasingDynamicStack()
        mdds.push(1)
        mdds.peek()
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
        mdds = MonotonicDecreasingDynamicStack()
        mdds.push(1)
        mdds.min_value()
        :return object(element in stack):
        """
        if not self.min_value_method:
            raise SystemError("Method not available! Create new stack with boolean min_value_method on True")
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.peek()

    def max_value(self) -> object:
        """
        Return maximum element in stack. Raise error if stack is empty.
        Be careful in usage, because if you store some different types in stack,
        method will throw exception during comparison between them.
        Time complexity amortized, so its O(1).
        Example of usages:
        mdds = MonotonicDecreasingDynamicStack()
        mdds.push(1)
        mdds.max_value()
        :return object(element in stack):
        """
        if not self.max_value_method:
            raise SystemError("Method not available! Create new stack with boolean max_value_method on True")
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[0]

    def length(self) -> int:
        """
        Return integer represent size(all elements store in stack) of stack.
        Time complexity amortized, so its O(1).
        Example of usages:
        mdds = MonotonicDecreasingDynamicStack()
        mdds.length()
        :return integer:
        """
        return self.stack.length()

    def is_empty(self) -> bool:
        """
        Return True if stack is empty, otherwise return False.
        Example of usages:
        mdds = MonotonicDecreasingDynamicStack()
        mdds.is_empty()
        :return boolean true of false:
        """
        return self.stack.is_empty()

    def clear(self) -> None:
        """
        Clear all data in stack.
        Example of usages:
        mdds = MonotonicDecreasingDynamicStack()
        for i in range(5):
            mdds.push(i)
        mdds.clear()
        :return None:
        """
        self.stack.clear()

    def all_methods(self) -> list[str]:
        """
        Returning list names of all available methods.
        Example of usages:
        mdds = MonotonicDecreasingDynamicStack()
        mdds.all_methods()
        :return list of strings:
        """
        return dir(MonotonicDecreasingDynamicStack)
