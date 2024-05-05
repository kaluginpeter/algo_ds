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
        self.array = array(self.definition_types.get(self.type))

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, new_capacity):
        raise ValueError("Capacity size cannot be changed after initialization")

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
        if self.size + 1 > self.capacity:
            raise IndexError("Array have max length of capacity. Can't append")
        if type(x) != self.type:
            raise ValueError(f"Object= {type(x)} should be {self.type} instance")
        self.array.append(x)
        self.size += 1

    def all_methods(self) -> list[str]:
        """
        Returning list names of all available methods.
        Example of usages:
        sota1 = StaticOneTypeArray()
        sota1.all_methods()
        :return list of strings:
        """
        return dir(StaticOneTypeArray)
