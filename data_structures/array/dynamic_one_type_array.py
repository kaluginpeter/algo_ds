import inspect
from array import array
from copy import deepcopy


class DynamicOneTypeArray:
    """
    Implementation of Dynamic one type array.
    Array can store either str or int, float instance type.
    Required arguments:
    First(optional) - type, either str or int or float. By default, sets to int type.
    For more information about all available methods,
    call all_methods methods. Example of usages:
    dota = DynamicOneTypeArray(int)
    dota.all_methods()
    """
    def __init__(self, type: str | int | float = int):
        self.definition_types: dict[type, str] = {
            str: 'u', int: 'q', float: 'd'
        }
        self.object_size: dict[str, int] = {
            'q': 8, 'u': 4, 'd': 8
        }
        self.string_representation: dict[type, chr | str] = {
            str: str, int: chr, float: str
        }
        if type not in self.definition_types:
            raise ValueError(f"Type= {type} should be either int or str or float instance")

        self._capacity = 10
        self.type = type
        self.size: int = 0
        if self.type != str:
            self.array = array(self.definition_types.get(self.type), [self.type(0) for _ in range(self.capacity)])
        else:
            self.array = list('0' for _ in range(self.capacity))

    def __rearrange_array(self, x: int = None) -> None:
        """
        Rearranging capacity of array.
        Use only in builtin functions.
        :param x:
        :return None:
        """
        if not any('capacity' in i or 'increase_capacity' in i for i in inspect.stack()):
            raise SystemError("Can't rearrange array forward this method")
        if x is not None and not isinstance(x, int):
            raise ValueError(f"Capacity type= {type(x)} should be int instance")
        if x is not None and x <= self.capacity:
            raise IndexError("Can't change capacity size less than current")
        if self.type == str:
            self.array += ['0' for _ in range((x - self.capacity) if x is not None else self.capacity)]
        else:
            self.array += array(self.definition_types.get(self.type), [self.type(0) for _ in range((x - self.capacity) if x is not None else self.capacity)])

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, new_capacity: int):
        if not isinstance(new_capacity, int):
            raise ValueError(f"Capacity type= {type(new_capacity)} should be int instance")
        if new_capacity <= self.capacity:
            raise IndexError("Can't change capacity size less than current")

        self.__rearrange_array(new_capacity)
        self._capacity = new_capacity

    def increase_capacity(self, x: int = None) -> None:
        """
        Increase capacity on given x if x is not give make capacity double more.
        Example of usages:
        dota = DynamicOneTypeArray()
        dota.increase_capacity()
        :param x: 
        :return None: 
        """
        if x is not None and not isinstance(x, int):
            raise ValueError(f"Capacity type= {type(x)} should be int instance")
        if x is not None and x <= self.capacity:
            raise IndexError("Can't change capacity size less than current")
        self.__rearrange_array(x)
        self.capacity += self.capacity if x is None else x

    def __str__(self) -> str:
        """
        Return string representation of array.
        Use for python builtin function str().
        Example of usages:
        dota = DynamicOneTypeArray()
        str(dota)
        :return string representation of array:
        """
        if self.is_empty():
            return '[]'
        output: list[str] = list()
        for i in range(self.length()):
            output.append(str(self.array[i]))
        return '[' + ', '.join(f"'{i}'" if self.type == str else i for i in output) + ']'

    def append(self, x) -> None:
        """
        Appending given element to array. Raise error if type is not as type defined in array.
        Example of usages:
        dota = DynamicOneTypeArray()
        dota.append(1)
        :param x:
        :return None:
        """
        if self.length() + 1 >= self.capacity:
            self.increase_capacity()
        if type(x) != self.type:
            raise ValueError(f"Object= {type(x)} should be {self.type} instance")
        self.array[self.length()] = x
        self.size += 1

    def __add__(self, x: array) -> array:
        """
        Make concatenation of array.
        Use for python builtin + operator.
        Example of usages:
        dota1 = DynamicOneTypeArray(int)
        dota2 = DynamicOneTypeArray(int)
        for i in range(5):
            dota2.append(i)
        dota1 + dota2
        :param x - array with same type of objects:
        :return result of concatenations array:
        """
        if not isinstance(x, array) and not isinstance(x, DynamicOneTypeArray):
            raise ValueError(f"Type= {type(x)} should be array instance")
        if self.length() + len(x) >= self.capacity:
            self.increase_capacity(self.length() + len(x))
        for i in x:
            if not isinstance(i, self.type):
                raise ValueError(f"Element= {i} type= {type(i)} should be= {self.type} instance")

        if self.type != str:
            output: DynamicOneTypeArray[str | int | float] = DynamicOneTypeArray(type=self.type)
        else:
            output: list[str] = list()
        idx: int = 0
        while idx < self.length():
            output.append(self.array[idx])
            idx += 1
        for i in x:
            output.append(i)
        return output

    def __iadd__(self, x: array) -> array:
        """
        Make concatenation of array.
        Use for python builtin += operator.
        Example of usages:
        dota1 = DynamicOneTypeArray(int)
        dota2 = DynamicOneTypeArray(int)
        for i in range(5):
            dota2.append(i)
        dota1 += dota2
        :param x - array with same type of objects:
        :return concatenated array:
        """
        return self.__add__(x)

    def __mul__(self, x: int) -> array:
        """
        Make multi concatenation of array x times.
        Use for python builtin * operator.
        Example of usages:
        dota = DynamicOneTypeArray()
        for i in range(2):
            dota.append(i)
        dota * 2
        :param x - integer represent reps of concatenating array:
        :return array object representing multi concatenation of array:
        """
        if not isinstance(x, int):
            raise ValueError(f"Type= {type(x)} of given object should be int instance")
        if self.length() * x >= self.capacity:
            self.increase_capacity(self.length() * x)

        if self.type != str:
            output: DynamicOneTypeArray[str | int | float] = DynamicOneTypeArray(type=self.type)
        else:
            output: list[str] = list()
        initial_array = [self.array[idx] for idx in range(self.length())]
        for i in range(x):
            if self.type != str:
                output.fromlist(initial_array)
            else:
                output += initial_array
        return output

    def __imul__(self, x: int) -> array:
        """
        Make multi concatenation of array x times.
        Use for python builtin *= operator.
        Example of usages:
        dota = DynamicOneTypeArray()
        for i in range(2):
            dota.append(i)
        dota *= 2
        :param x - integer represent reps of concatenating array:
        :return array object representing multi concatenation of array:
        """
        return self.__mul__(x)

    def __rmul__(self, x: int) -> array:
        """
        Make multi inverse concatenation of array x times.
        Use for python builtin * operator.
        Example of usages:
        dota = DynamicOneTypeArray()
        for i in range(2):
            dota.append(i)
        2 * dota
        :param x - integer represent reps of concatenating array:
        :return array object representing multi inverse concatenation of array:
        """
        return self.__mul__(x)

    def __setitem__(self, idx: int, value: str | int | float) -> None:
        """
        Set given value at given index position.
        Index may be negative.
        Use for python builtin [] method.
        Example of usages:
        dota = DynamicOneTypeArray()
        dota.append(1)
        dota[0] = 0
        :param idx - index position in array:
        :param value - value that be inserted:
        :return None:
        """
        if not isinstance(idx, int):
            raise IndexError(f"Given type= {type(idx)} of index should be int instance")
        if not isinstance(value, self.type):
            raise ValueError(f"Given type= {type(value)} of object should be {self.type} instance")

        is_negative_index: bool = idx < 0
        if is_negative_index:
            idx = self.length() - abs(idx)
        if not 0 <= idx < self.length():
            raise IndexError("Array index out of range")
        self.array[idx] = value

    def extend(self, x: iter) -> None:
        """
        Extending given iterable sequence in array.
        Example of usages:
        dota = DynamicOneTypeArray()
        dota.extend([1, 2, 3])
        :param x:
        :return None:
        """
        if not hasattr(x, '__iter__'):
            raise TypeError(f"Sequence= {type(x)} should be iterable for extending")
        if self.length() + len(x) >= self.capacity:
            self.increase_capacity(self.length() + len(x))
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
        dota = DynamicOneTypeArray()
        dota.insert(555, 0)
        :param pos index for insertion element:
        :param x:
        :return None:
        """
        if self.length() + 1 >= self.capacity:
            self.increase_capacity()
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
        stack: DynamicOneTypeArray = DynamicOneTypeArray(type=self.type)
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
        dota = DynamicOneTypeArray()
        dota.append(1)
        dota.pop()
        :idx index of element in array
        :return deleted element:
        """
        if self.is_empty():
            raise IndexError("Can't delete from empty array")

        if idx is None:
            idx = self.length() - 1
        start_idx: int = idx
        is_negative_position: bool = idx < 0
        if is_negative_position:
            idx = self.length() - abs(idx)
        if not 0 <= idx < self.length():
            raise IndexError(f"Pop index= {start_idx} out of range")

        if idx == self.length() - 1:
            val: str | int | float = self.array[idx]
            self.size -= 1
            return val

        val: str | int | float = self.array[idx]
        stack: DynamicOneTypeArray = DynamicOneTypeArray(type=self.type)
        for i in range(idx + 1, self.length()):
            stack.append(self.array[i])

        inner_idx_for_stack: int = 0
        for i in range(self.length() - idx - 1):
            self.array[idx] = stack[inner_idx_for_stack]
            idx += 1
            inner_idx_for_stack += 1
        self.size -= 1
        return val

    def remove(self, x: any) -> str | int | float:
        """
        Removing first occurrences of given element if it consists in array.
        Example of usages:
        dota = DynamicOneTypeArray()
        dota.append(1)
        dota.remove(1)
        :param x:
        :return deleted element:
        """
        if self.is_empty():
            raise IndexError("Can't delete from empty array")
        if not self.contains(x):
            raise ValueError(f"Element= {x} not in array")

        idx: int = 0
        while idx < self.length():
            if self.array[idx] == x:
                return self.pop(idx)
            idx += 1

    def __delitem__(self, idx: int) -> None:
        """
        Delete element at given index in array.
        Use for python builtin del function.
        Example of usages:
        dota = DynamicOneTypeArray()
        dota.append(1)
        del dota[0]
        :param idx:
        :return None:
        """
        self.pop(idx)

    def fromlist(self, x: list) -> None:
        """
        Appending all elements from given list to array.
        Example of usages:
        dota = DynamicOneTypeArray()
        dota.fromlist([1, 2, 3])
        :param x:
        :return None:
        """
        if not isinstance(x, list):
            raise ValueError(f"Given object= {type(x)} should be list instance")

        return self.extend(x)

    def tolist(self) -> list[str | int | float]:
        """
        Return list contains all elements in array.
        Example of usages:
        dota = DynamicOneTypeArray()
        for i in range(5):
            dota.append(i)
        dota.tolist()
        :return all elements existing in array in list object:
        """
        output: list[str | int | float] = list()
        idx: int = 0
        while idx < self.length():
            output.append(self.array[idx])
            idx += 1
        return output

    def clear(self) -> None:
        """
        Clear all data in array.
        Example of usages:
        dota = DynamicOneTypeArray()
        for i in range(5):
            dota.append(i)
        dota.clear()
        :return None:
        """
        self.size = 0
        if self.type != str:
            self.array = array(self.definition_types.get(self.type), [self.type(0) for _ in range(self.capacity)])
        else:
            self.array = list('0' for _ in range(self.capacity))

    def length(self) -> int:
        """
        Return length of array.
        Example of usages:
        dota = DynamicOneTypeArray()
        dota.length()
        :return int instance representation length of array:
        """
        return self.size

    def __len__(self) -> int:
        """
        Returning length of array length.
        Using for python builtin in function.
        Example of usages:
        dota = DynamicOneTypeArray()
        len(dota)
        :return int representation of length array:
        """
        return self.length()

    def is_empty(self) -> bool:
        """
        Return true is array is empty.
        Example of usages:
        dota = DynamicOneTypeArray()
        dota.is_empty()
        :return boolean true or false:
        """
        return self.length() == 0

    def contains(self, x: any) -> bool:
        """
        Return true if given element exist in array.
        Example of usages:
        dota = DynamicOneTypeArray()
        dota.contains(5)
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
        dota = DynamicOneTypeArray()
        5 in dota
        :param x:
        :return boolean true of false:
        """
        return self.contains(x)

    def __getitem__(self, x: any) -> int:
        """
        Return element at given index in array. Indexing starts with 0.
        Use for python builtin [] index function. Index may be negative.
        Example of usages:
        dota = DynamicOneTypeArray()
        dota.append(0)
        dota[0]
        :param x:
        :return int index of element if array:
        """
        if not isinstance(x, int):
            raise ValueError(f"Type of given index= {type(x)} should be int instance")
        initial_index: int = x
        is_negative_index: bool = x < 0
        if is_negative_index:
            x = self.length() - abs(x)

        if not 0 <= x < self.length():
            raise IndexError(f"List index= {initial_index} out of range")

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
        dota = DynamicOneTypeArray()
        dota.append(1)
        dota.index(1)
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

    def sort(self, key: any = None, reverse: bool = False) -> None:
        """
        Sort array in place by given key and reverse variable.
        Example of usages:
        dota = DynamicOneTypeArray()
        for i in range(5):
            dota.append(i)
        dota.sort(reverse=True)
        :param key(optional, by default None) - can be builtin variable or lambda expression:
        :param reverse(optional, by default False) - boolean true of false:
        :return None:
        """
        output: list[str | int | float] = [self.array[idx] for idx in range(self.length())]
        output.sort(key=key, reverse=reverse)
        if self.type != str:
            self.clear()
            self.fromlist(output)
            return
        self.array = output + [0 for _ in range(self.capacity - self.length())]

    def deepcopy(self) -> array:
        """
        Make deepcopy of array.
        Example of usages:
        dota = DynamicOneTypeArray()
        for i in range(5):
            dota.append(i)
        dota.deepcopy()
        :return copy array:
        """
        if self.type != str:
            output: DynamicOneTypeArray[str | int | float] = DynamicOneTypeArray(type=self.type)
        else:
            output: list[str] = list()
        idx: int = 0
        while idx < self.length():
            output.append(deepcopy(self.array[idx]))
            idx += 1
        return output

    def __deepcopy__(self, memodict={}) -> array:
        """
        Make deepcopy of array.
        Use for copy.deepcopy() method
        Example of usages:
        from copy import deepcopy
        dota = DynamicOneTypeArray()
        for i in range(5):
            dota.append(i)
        deepcopy(dota)
        :return copy array:
        """
        return self.deepcopy()

    def copy(self) -> array:
        """
        Make copy(shallow copy) of array.
        Example of usages:
        dota = DynamicOneTypeArray()
        for i in range(5):
            dota.append(i)
        dota.copy()
        :return copy array:
        """
        output = self
        return output

    def __copy__(self) -> array:
        """
        Make copy(shallow copy) of array.
        Use for copy.copy method.
        Example of usages:
        from copy import copy
        dota = DynamicOneTypeArray()
        for i in range(5):
            dota.append(i)
        copy(dota)
        :return copy array:
        """
        return self.copy()

    def count(self, x: any) -> int:
        """
        Return count of all occurrences element in array.
        Example of usages:
        dota = DynamicOneTypeArray()
        dota.count(1)
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

    def reverse(self) -> None:
        """
        Reverse array.
        Time complexity O(N).
        Memory complexity O(1).
        Example of usages:
        dota = DynamicOneTypeArray()
        dota.reverse()
        :return None:
        """
        left, right = 0, self.length() - 1
        while left < right:
            self.array[left], self.array[right] = self.array[right], self.array[left]
            left, right = left + 1, right - 1

    def __reversed__(self) -> iter:
        """
        Return iterator with reversing sequence of array.
        Use for python builtin reversed() function.
        Example of usages:
        dota = DynamicOneTypeArray()
        for i in range(5):
            dota.append(i)
        reversed(dota)
        :return iterator with reversing sequence of array:
        """
        return reversed([self.array[idx] for idx in range(0, self.length())])

    def __iter__(self) -> iter:
        """
        Return iterator with sequence of array elements.
        Use for python builtin iter() function.
        Example of usages:
        dota = DynamicOneTypeArray()
        for i in range(5):
            dota.append(i)
        iter(dota)
        :return iterator with elements in array sequence:
        """
        return iter([self.array[idx] for idx in range(0, self.length())])

    def typecode(self) -> str:
        """
        Return one character of string representation type objects in array in C language.
        Example of usages:
        dota = DynamicOneTypeArray()
        dota.typecode()
        :return string character:
        """
        return self.definition_types.get(self.type)

    def itemsize(self) -> int:
        """
        Return integer represent every item size in array in bytes.
        Example of usages:
        dota = DynamicOneTypeArray()
        dota.itemsize()
        :return integer:
        """
        return self.object_size.get(self.typecode())

    def all_methods(self) -> list[str]:
        """
        Returning list names of all available methods.
        Example of usages:
        dota = DynamicOneTypeArray()
        dota.all_methods()
        :return list of strings:
        """
        return dir(DynamicOneTypeArray)
