from node import Node


class CircularLinkedList:
    """
    Implementation of circular linked list.
    To see all available methods use all_methods method.
    Example of usages:
    cll1 = CircularLinkedList()
    cll1.all_methods()
    """
    def __init__(self, head: Node | None = None):
        self.head: Node | None = head
        self.tail: Node | None = self.head
        self.size: int = 0

    def __str__(self) -> str:
        """
        Returning string representation on linked list in follow type:
        Value_of_Node->Next_value_of_Node...->None
        """
        if self.size == 0:
            return 'None'
        output: list[str] = list()
        tmp: Node = self.head
        while tmp is not self.tail:
            output.append(str(tmp))
            tmp = tmp.next
        output.append(str(self.tail))
        output.append('None')
        return '->'.join(output)

    def all_methods(self) -> list[str]:
        """
        Returning list names of all available methods.
        Example of usages:
        cll1 = CircularLinkedList()
        cll1.all_methods()
        :return list of strings:
        """
        return dir(CircularLinkedList)

    def append(self, x: any) -> None:
        """
        Appending given param x to the end(in tail) of linked list.
        x - any type of class.
        Example of usages:
        cll1 = CircularLinkedList()
        for i in range(4):
            cll1.append(i)
        :param x:
        :return None:
        """

        if self.is_empty():
            self.head = Node(data=x)
            self.tail = self.head
            self.tail.next = self.head
            self.size += 1
            return

        self.tail.next = Node(data=x)
        self.tail = self.tail.next
        self.tail.next = self.head
        self.size += 1

    def insert(self, pos: int, x: any) -> None:
        """
        Insert element at given index in list. List indexing starts with 0.
        Index may be negative.
        First param is index, second - element.
        Example of usages:
        cll1 = CircularLinkedList()
        cll1.insert(0, 1)
        :param pos:
        :param x:
        :return None:
        """
        if self.is_empty():
            self.head = Node(data=x)
            self.tail = self.head
            self.tail.next = self.head
            self.size += 1
            return

        is_negative_position: bool = pos < 0
        if pos == 0 or (is_negative_position and abs(pos) >= self.length()):
            self.head = Node(data=x, next=self.head)
            self.tail.next = self.head
            self.size += 1
            return

        elif pos >= self.length():
            self.tail.next = Node(data=x, next=self.head)
            self.tail = self.tail.next
            self.size += 1
            return

        if is_negative_position:
            pos = self.length() - abs(pos)

        idx: int = 0
        tmp: Node = self.head
        while idx < pos - 1:
            idx += 1
            tmp = tmp.next
        tmp.next = Node(data=x, next=tmp.next)
        self.size += 1

    def length(self) -> int:
        """
        Returning length of linked list.
        Time complexity O(1).
        Example usages:
        cll1 = CircularLinkedList()
        cll1.length()
        :return length of linked list:
        """
        return self.size

    def __len__(self) -> int:
        """
        Returning length of liked list.
        Use this for python builtin len() method.
        Time complexity O(1).
        Example of usages:
        cll1 = CircularLinkedList()
        len(cll1)
        :return length of linked list:
        """
        return self.length()

    def is_empty(self) -> bool:
        """
        Return true if linked list is empty, otherwise return False
        Example of usages:
        cll1 = CircularLinkedList()
        cll1.is_empty()
        :return boolean type True or False:
        """
        return self.length() == 0

    def contains(self, x: any) -> bool:
        """
        Returning true if element or Node exists in linked list nodes data, otherwise return false
        Example of usages:
        cll1 = CircularLinkedList()
        for i in range(4):
            cll1.append(i)
        x = ll1.head
        cll1.contains(x) or cll1.contains(0)
        :param x:
        :return boolean type of True and False:
        """
        if isinstance(x, Node) and self.contains_node(x):
            return self.contains_node(x)
        if self.is_empty():
            return False
        tmp: Node = self.head
        self.tail.next = None
        while tmp:
            if tmp.data == x or tmp.data is x:
                self.tail.next = self.head
                return True
            tmp = tmp.next
        self.tail.next = self.head
        return False

    def __contains__(self, x: any) -> bool:
        """
        Returning true if element or Node exists in linked list, otherwise return false.
        Use for builtin python "in" function.
        Example of usages:
        cll1 = CircularLinkedList()
        x = 5
        x in cll1
        :param x:
        :return boolean type of True and False:
        """
        if isinstance(x, Node) and self.contains_node(x):
            return self.contains_node(x)
        return self.contains(x)

    def contains_node(self, x: Node) -> bool:
        """
        Returning True if given Node exists in linked list nodes, otherwise return False.
        Example of usages:
        cll1 = CircularLinkedList()
        x = Node(data=5)
        cll1.contains_node(x)
        :param x:
        :return boolean type of True and False:
        """
        if not isinstance(x, Node):
            raise ValueError(f"{type(x)} should be Node instance")
        if self.is_empty():
            return False
        tmp: Node = self.head
        self.tail.next = None
        while tmp:
            if tmp is x:
                self.tail.next = self.head
                return True
            tmp = tmp.next
        self.tail.next = self.head
        return False

    def pop(self) -> Node:
        """
        Deleting last element in linked list.
        Raise ValueError if list is empty.
        Example of usages:
        cll1 = CircularLinkedList()
        cll1.append(1)
        cll1.pop()
        :return data of object Node instance:
        """
        if self.is_empty():
            raise IndexError("Can't delete from empty linked list")
        if self.length() == 1:
            val: Node = self.head
            self.head = None
            self.tail = self.head
            self.size -= 1
            return val
        self.tail.next = None
        tmp: Node = self.head
        while tmp.next.next:
            tmp = tmp.next
        val: Node = tmp.next
        tmp.next = self.head
        self.tail = tmp
        self.size -= 1
        return val

    def remove(self, x: any) -> Node:
        """
        Remove first occurrences of given element/Node in list nodes data and return it Node instance.
        Example of usages:
        cll1 = CircularLinkedList()
        x = Node(data=5)
        cll1.append(x.data)
        cll1.remove(x.data)
        :param x:
        :return data of instance Node class:
        """
        if self.is_empty():
            raise IndexError("Can't remove from empty linked list")
        if isinstance(x, Node) and self.contains_node(x):
            return self.remove_node(x)
        if not self.contains(x):
            raise ValueError(f"Element {x} not in linked list")

        if self.length() == 1:
            val: Node = self.head
            self.head = None
            self.tail = self.head
            self.size -= 1
            return val.data

        if self.head.data == x or self.head.data is x:
            val: Node = self.head
            self.head = self.head.next
            self.tail.next = self.head
            self.size -= 1
            return val.data

        self.tail.next = None
        tmp: Node = self.head
        while tmp.next:
            if tmp.next.data == x or tmp.next.data is x:
                val: Node = tmp.next
                tmp.next = tmp.next.next
                if val is self.tail:
                    self.tail = tmp
                    self.tail.next = self.head
                self.size -= 1
                return val.data
            tmp = tmp.next

    def remove_node(self, x: Node) -> Node:
        """
        Remove given Node instance from linked list and return it.
        Example of usages:
        cll1 = CircularLinkedList()
        x = Node(data=1)
        cll1.append(x.data)
        cll1.remove_node(x)
        :param x:
        :return Instance of Node class:
        """
        if self.is_empty():
            raise IndexError("Can't remove from empty linked list")
        if not self.contains_node(x):
            raise ValueError(f"Node {x} not in linked list")

        if self.length() == 1:
            val: Node = self.head
            self.head = None
            self.tail = self.head
            self.size -= 1
            return val

        if self.head is x:
            val: Node = self.head
            self.head = self.head.next
            self.tail.next = self.head
            self.size -= 1
            return val

        self.tail.next = None
        tmp: Node = self.head
        while tmp.next:
            if tmp.next is x:
                val: Node = tmp.next
                tmp.next = tmp.next.next
                if val is self.tail:
                    self.tail = tmp
                    self.tail.next = self.head
                self.size -= 1
                return val
            tmp = tmp.next

    def remove_at(self, x: int) -> Node:
        """
        Removing Node at given position. Indexing of linked list starts with 1.
        Example of usages:
        cll1 = CircularLinkedList()
        for i in range(10):
            cll1.append(i)
        cll1.remove_at(10)
        :param x:
        :return Instance of Node class:
        """
        if self.is_empty():
            raise IndexError("Can't remove from empty linked list")
        if not 1 <= x <= self.length():
            raise IndexError(f"Linked list index= {x} out of range")
        if self.length() == 1 or x == 1:
            return self.remove_node(self.head)
        idx: int = 1
        tmp: Node = self.head
        while idx < x:
            idx += 1
            tmp = tmp.next
        return self.remove_node(tmp)

    def reverse(self) -> None:
        """
        Reversing linked list. Time Complexity is O(N) and Memory Complexity is O(1).
        Example of usages:
        cll1 = CircularLinkedList()
        for i in range(5):
            cll1.append(i)
        cll1.reverse()
        :return None:
        """
        if self.is_empty():
            raise ValueError("Can't reverse empty linked list")

        prev: Node | None = None
        current: Node = self.head
        self.tail.next = None
        initial_node: Node = self.head
        while current:
            nxt: Node = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev
        self.tail = initial_node
        self.tail.next = self.head

    def clear(self) -> None:
        """
        Clear all elements in linked list.
        Time complexity O(1).
        Example of usages:
        cll1 = CircularLinkedList()
        for i in range(10):
            cll1.append(i)
        cll1.clear()
        :return None:
        """
        self.head = None
        self.size = 0
