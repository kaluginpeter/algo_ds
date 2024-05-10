from data_structures.arrays.static_multi_type_array import StaticMultiTypeArray


class StaticStack:
    """
    Implementation of Static Stack data structure.
    Static stack using Static Multi Type Array for storing objects.
    Static stack can store only one of the different data types, because
    implementation use some amortized operation and attempting to push
    some different types of object will throw an exception.
    Required params:
    capacity: int - optional, by default sets to 10. Capacity will define size of stack.
    Example of usages:
    ss = StaticStack(10)
    For more information about available methods use all_methods() methods, like:
    ss.all_methods()
    """
    def __init__(self, capacity: int = 10):
        self.stack: StaticMultiTypeArray = StaticMultiTypeArray(capacity=capacity)
        self.minimum_value_in_stack: StaticMultiTypeArray = StaticMultiTypeArray(capacity=capacity)

    def push(self, x: any) -> None:
        """
        Push element to the top of stack.
        Be careful in usage when attempting push object with different data type,
        stack use amortized min_value method, so pushing will throw exception during comparison elements.
        Raise error if stack is full(have max size of defined capacity).
        Time complexity is O(1).
        Example of usages:
        ss = StaticStack()
        ss.push(1)
        :param x:
        :return None:
        """
        self.stack.append(x)
        if self.minimum_value_in_stack.is_empty():
            self.minimum_value_in_stack.append(x)
            return
        if x > self.minimum_value_in_stack[-1]:
            self.minimum_value_in_stack.append(self.min_value())
            return
        self.minimum_value_in_stack.append(x)

    def pop(self) -> object:
        """
        Pop element from the top of stack and return it.
        Raise error if stack is empty.
        Time complexity is O(1).
        Example of usages:
        ss = StaticStack()
        ss.push(1)
        ss.pop()
        :return object(popped element):
        """
        self.minimum_value_in_stack.pop()
        return self.stack.pop()

    def peek(self) -> object:
        """
        Return last(from the top) element from the stack.
        Raise error if stack is empty.
        Time complexity is O(1)
        Example of usages:
        ss = StaticStack()
        ss.push(1)
        ss.peek()
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
        ss = StaticStack()
        ss.push(1)
        ss.min_value()
        :return object(element in stack):
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.minimum_value_in_stack[-1]

    def length(self) -> int:
        """
        Return integer represent size(all elements store in stack) of stack.
        Time complexity amortized, so its O(1).
        Example of usages:
        ss = StaticStack()
        ss.length()
        :return integer:
        """
        return self.stack.length()

    def is_empty(self) -> bool:
        """
        Return True if stack is empty, otherwise return False.
        Example of usages:
        ss = StaticStack()
        ss.is_empty()
        :return boolean true of false:
        """
        return self.stack.is_empty()

    def is_full(self) -> bool:
        """
        Return True if stack is full(have max elements in their size), otherwise return False.
        Example of usages:
        ss = StaticStack()
        ss.is_full()
        :return boolean true of false:
        """
        return self.stack.length() == self.stack.capacity

    def all_methods(self) -> list[str]:
        """
        Returning list names of all available methods.
        Example of usages:
        ss = StaticStack()
        ss.all_methods()
        :return list of strings:
        """
        return dir(StaticStack)
