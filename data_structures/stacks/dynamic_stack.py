from data_structures.arrays.dynamic_multi_type_array import DynamicMultiTypeArray


class DynamicStack:
    """
    Implementation of Dynamic Stack data structure.
    Static stack using Dynamic Multi TypeArray for storing objects.
    Static stack can store only one of the different data types, because
    implementation use some amortized operation and attempting to push
    some different types of object will throw an exception.
    Required params:
    min_value_method: bool optional, by default sets to false. If true keep track minimum value in stack
    max_value_method: bool optional, by default sets to false. It true keep track maximum value in stack
    Example of usages:
    ds = DynamicStack(10)
    For more information about available methods use all_methods() methods, like:
    ds.all_methods()
    """
    def __init__(self, min_value_method: bool = False, max_value_method: bool = False):
        self.stack: DynamicMultiTypeArray = DynamicMultiTypeArray()
        self.min_value_method = min_value_method
        self.max_value_method = max_value_method
        if self.min_value_method:
            self.minimum_value_in_stack: DynamicMultiTypeArray = DynamicMultiTypeArray()
        if self.max_value_method:
            self.maximum_value_in_stack: DynamicMultiTypeArray = DynamicMultiTypeArray()

    def push(self, x: any) -> None:
        """
        Push element to the top of stack.
        Be careful in usage when attempting push object with different data type,
        stack use amortized min_value method, so pushing will throw exception during comparison elements.
        Time complexity is O(1).
        Example of usages:
        ds = DynamicStack()
        ds.push(1)
        :param x:
        :return None:
        """
        self.stack.append(x)

        if self.length() == 1:
            if self.min_value_method:
                self.minimum_value_in_stack.append(x)
            if self.max_value_method:
                self.maximum_value_in_stack.append(x)
            return

        if self.min_value_method:
            self.minimum_value_in_stack.append(self.min_value() if x > self.maximum_value_in_stack[-1] else x)

        if self.max_value_method:
            self.maximum_value_in_stack.append(x if x > self.maximum_value_in_stack[-1] else self.max_value())

    def pop(self) -> object:
        """
        Pop element from the top of stack and return it.
        Raise error if stack is empty.
        Time complexity is O(1).
        Example of usages:
        ds = DynamicStack()
        ds.push(1)
        ds.pop()
        :return object(popped element):
        """
        if self.min_value_method:
            self.minimum_value_in_stack.pop()
        if self.max_value_method:
            self.maximum_value_in_stack.pop()
        return self.stack.pop()

    def peek(self) -> object:
        """
        Return last(from the top) element from the stack.
        Raise error if stack is empty.
        Time complexity is O(1)
        Example of usages:
        ds = DynamicStack()
        ds.push(1)
        ds.peek()
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
        ds = DynamicStack()
        ds.push(1)
        ds.min_value()
        :return object(element in stack):
        """
        if not self.min_value_method:
            raise SystemError("Method not available! Make boolean min_value_method on True before usage")
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.minimum_value_in_stack[-1]

    def max_value(self) -> object:
        """
        Return maximum element in stack. Raise error if stack is empty.
        Be careful in usage, because if you store some different types in stack,
        method will throw exception during comparison between them.
        Time complexity amortized, so its O(1).
        Example of usages:
        ds = DynamicStack()
        ds.push(1)
        ds.max_value()
        :return object(element in stack):
        """
        if not self.max_value_method:
            raise SystemError("Method not available! Make boolean max_value_method on True before usage")
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.maximum_value_in_stack[-1]

    def length(self) -> int:
        """
        Return integer represent size(all elements store in stack) of stack.
        Time complexity amortized, so its O(1).
        Example of usages:
        ds = DynamicStack()
        ds.length()
        :return integer:
        """
        return self.stack.length()

    def is_empty(self) -> bool:
        """
        Return True if stack is empty, otherwise return False.
        Example of usages:
        ds = DynamicStack()
        ds.is_empty()
        :return boolean true of false:
        """
        return self.stack.is_empty()

    def all_methods(self) -> list[str]:
        """
        Returning list names of all available methods.
        Example of usages:
        ds = DynamicStack()
        ds.all_methods()
        :return list of strings:
        """
        return dir(DynamicStack)