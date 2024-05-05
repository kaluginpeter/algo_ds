from array import array


class StaticOneTypeArray:
    """
    Implementation of static one type array.
    Array can store either str or int, float instance type.
    Required arguments:
    First(optional) - type, either str or int or float. By default, sets to int type.
    Second(optional)- int, capacity. Set max length of size array. By default, sets to 10.
    For more information about all available methods,
    call all_methods methods. Example of usages:
    sota1 = StaticOneTypeArray(int, 10)
    sota1.all_methods()
    """
    def __init__(self, type: str | int | float = int, capacity: int = 10):
        self.definition_types: dict[type, str] = {
            str: 'u', int: 'q', float: 'd'
        }
        self.string_representation: dict[type, chr | str] = {
            str: str, int: chr, float: str
        }
        if type not in self.definition_types:
            raise ValueError(f"Type= {type} should be either int or str or float instance")
        if not isinstance(capacity, int):
            raise ValueError(f"Capacity type= {capacity} should be int instance")
        if capacity < 1:
            raise ValueError(f"Capacity= {capacity} can't be less than one")
        if capacity == float('inf'):
            raise ValueError(f"Capacity= {capacity} can't have infinity length")

        self._capacity = capacity
        self.type = type
        self.size: int = 0
        self.array = array(self.definition_types.get(self.type), [self.type(0) for _ in range(self.capacity)])

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, new_capacity):
        raise ValueError("Capacity size cannot be changed after initialization")

    def __str__(self) -> str:
        """
        Return string representation of array.
        Use for python builtin function str().
        Example of uages:
        sota1 = StaticOneTypeArray()
        str(sota1)
        :return string representation of array:
        """
        if self.is_empty():
            return '[]'
        output: list[str] = list()
        for i in range(self.length()):
            output.append(str(self.array[i]))
        return '[' + ', '.join(f"'{i}'" if self.type == str else str(i) for i in output) + ']'

    def append(self, x) -> None:
        """
        Appending given element to array. Raise error if type is not as type defined in array.
        Raise error if size of array is equal to capacity(i.e. array has max size).
        Example of usages:
        sota1 = StaticOneTypeArray()
        sota1.append(1)
        :param x:
        :return None:
        """
        if self.length() + 1 > self.capacity:
            raise IndexError("Array have max length of capacity. Can't append")
        if type(x) != self.type:
            raise ValueError(f"Object= {type(x)} should be {self.type} instance")
        self.array[self.length()] = x
        self.size += 1

    def extend(self, x: iter) -> None:
        """
        Extending given iterable sequence in array.
        Example of usages:
        sota1 = StaticOneTypeArray()
        sota1.extend([1, 2, 3])
        :param x:
        :return None:
        """
        if not hasattr(x, '__iter__'):
            raise TypeError(f"Sequence= {type(x)} should be iterable for extending")
        if self.length() + len(x) > self.capacity:
            raise IndexError("Length of given sequence can't be added in array, capacity will be overload!")

        for i in x:
            if not isinstance(i, self.type):
                raise ValueError(f"Object= {i} should be {self.type} instance")

        for i in x:
            self.append(i)

    def insert(self, pos: int, x: any) -> None:
        """
        Insert element at given postion.
        Array indexing starts with 0. Index can be negative.
        Example of usages:
        sota1 = StaticOneTypeArray()
        sota1.insert(555, 0)
        :param pos index for insertion element:
        :param x:
        :return None:
        """
        if self.length() + 1 > self.capacity:
            raise ValueError("Capacity if full. Can't insert in full array")
        if not isinstance(x, self.type):
            raise ValueError(f"Object= {type(x)} should be {self.type} instance")

        if pos >= self.length():
            return self.append(x)

        is_negative_position: bool = pos < 0
        if is_negative_position:
            pos = max(self.length() - abs(pos), 0)
        idx: int = 0
        while idx < pos:
            idx += 1
        stack: StaticOneTypeArray = StaticOneTypeArray(type=self.type, capacity=self.length() - idx)
        stack.append(x)
        self.size += 1
        for i in range(self.length() + 1 - idx):
            old_item = self.array[idx]
            self.array[idx] = stack.pop()
            stack.append(old_item)
            idx += 1

    def pop(self, idx: int | None = None) -> str | int | float:
        """
        Delete element from given index or from the end of array if index not given.
        Indexing of array starts with 0. Index can be negative
        Example of usages:
        sota1 = StaticOneTypeArray()
        sota1.append(1)
        sota1.pop()
        :idx index of element in array
        :return deleted element:
        """
        if self.is_empty():
            raise IndexError("Can't delete from empty list")

        if idx is None:
            idx = self.length() - 1
        start_idx: int = idx
        is_negative_position: bool = idx < 0
        if is_negative_position:
            idx = self.length() - abs(idx)
        if not 0 <= idx < self.length():
            raise IndexError(f"Pop index= {start_idx} out of range")

        if idx == self.length() - 1:
            val: str | int| float = self.array[idx]
            self.size -= 1
            return val

        val: str | int | float = self.array[idx]
        stack: StaticOneTypeArray = StaticOneTypeArray(type=self.type, capacity=self.length() - idx - 1)
        for i in range(idx + 1, self.length()):
            stack.append(self.array[i])

        inner_idx_for_stack: int = 0
        for i in range(self.length() - idx - 1):
            self.array[idx] = stack[inner_idx_for_stack]
            idx += 1
            inner_idx_for_stack += 1
        self.size -= 1
        return val

    def fromlist(self, x: list) -> None:
        """
        Appending all elements from given list to array.
        Example of usages:
        sota1 = StaticOneTypeArray()
        sota1.fromlist([1, 2, 3])
        :param x:
        :return None:
        """
        if not isinstance(x, list):
            raise ValueError(f"Given object= {type(x)} should be list instance")

        return self.extend(x)

    def clear(self) -> None:
        """
        Clear all data in array.
        Example of usages:
        sota1 = StaticOneTypeArray()
        for i in range(5):
            sota1.append(i)
        sota1.clear()
        :return None:
        """
        self.size = 0
        self.array = array(self.definition_types.get(self.type), [self.type(0) for _ in range(self.capacity)])

    def length(self) -> int:
        """
        Return length of array.
        Example of usages:
        sota1 = StaticOneTypeArray()
        sota1.length()
        :return int instance representation length of array:
        """
        return self.size

    def __len__(self) -> int:
        """
        Returning length of array length.
        Using for python builtin in function.
        Example of usages:
        sota1 = StaticOneTypeArray()
        len(sota1)
        :return int representation of length array:
        """
        return self.length()

    def is_empty(self) -> bool:
        """
        Return true is array is empty.
        Example of usages:
        sota1 = StaticOneTypeArray()
        sota1.is_empty()
        :return boolean true or false:
        """
        return self.length() == 0

    def contains(self, x: any) -> bool:
        """
        Return true if given element exist in array.
        Example of usages:
        sota1 = StaticOneTypeArray()
        sota1.contains(5)
        :param x:
        :return boolean true or false:
        """
        if self.is_empty():
            return False

        idx: int = 0
        while idx < self.length():
            if self.array[idx] == x:
                return True
            idx += 1
        return False

    def __contains__(self, x: any) -> bool:
        """
        Return true if given element exist in array.
        Using for python builtin "in" function.
        Example of usages:
        sota1 = StaticOneTypeArray()
        5 in sota1
        :param x:
        :return boolean true of false:
        """
        return self.contains(x)

    def __getitem__(self, x: any) -> int:
        """
        Return element at given index in array. Indexing starts with 0.
        Use for python builtin [] index function.
        Example of usages:
        sota1 = StaticOneTypeArray()
        sota1.append(0)
        sota1[0]
        :param x:
        :return int index of element if array:
        """
        if not 0 <= x < self.length():
            raise IndexError(f"List index= {x} out of range")

        idx: int = 0
        while idx < self.length():
            if idx == x:
                return self.array[idx]
            idx += 1

    def index(self, x: any) -> bool:
        """
        Return index of first occurrences given element in array if it exists.
        Indexing starts with 0.
        Example of usages:
        sota1 = StaticOneTypeArray()
        sota1.append(1)
        sota1.index(1)
        :param x:
        :return int index position of first occurrences given element:
        """
        if not self.contains(x):
            raise ValueError(f"Element= {x} not in array")

        idx: int = 0
        while idx < self.length():
            if self.array[idx] == x:
                return idx
            idx += 1

    def count(self, x: any) -> int:
        """
        Return count of all occurrences element in array.
        Example of usages:
        sota1 = StaticOneTypeArray()
        sota1.count(1)
        :param x:
        :return integer representing count of given element in array:
        """
        if self.is_empty():
            return 0

        output: int = 0
        idx: int = 0
        while idx < self.length():
            if self.array[idx] == x:
                output += 1
            idx += 1
        return output

    def all_methods(self) -> list[str]:
        """
        Returning list names of all available methods.
        Example of usages:
        sota1 = StaticOneTypeArray()
        sota1.all_methods()
        :return list of strings:
        """
        return dir(StaticOneTypeArray)
