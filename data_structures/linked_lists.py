class Node:
    """
    Implementation of part Node to Abstract List Data Structure.
    Take a two type of arguments:
    data - required, item that been in list.
    next - optional(in default sets to None), pointer to next DoubleNode instance.
    """
    def __init__(self, data: any, next: object | None = None):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """
        Returning string representation on Node in follow way:
        "data_of_node"
        :return str type:
        """
        return f'{self.data}'


class DoubleNode:
    """
    Implementation Node with existing previous and next pointers.
    Take a three type of arguments:
    data - required, item that been in list.
    next - optional(in default sets to None), pointer to next DoubleNode instance.
    prev - optional(in default sets to None), pointer to previous DoubleNode instance.
    """
    def __init__(self, data: any, next: object | None = None, prev: object | None = None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        """
        Returning string representation on Node in follow way:
        "data_of_node"
        :return str type:
        """
        return f'{self.data}'


class SingleLinkedList:
    """
    Implementation of single linked list.
    To see all available methods use all_methods method.
    Example of usages:
    ll1 = SingleLinkedList()
    ll1.all_methods()
    """
    def __init__(self, head: Node | None = None):
        self.head: Node | None = head
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
        while tmp:
            output.append(str(tmp))
            tmp = tmp.next
        output.append('None')
        return '->'.join(output)

    def all_methods(self) -> list[str]:
        """
        Returning list of names all available methods
        :return list of strings:
        """
        return dir(SingleLinkedList)

    def append(self, x: any) -> None:
        """
        Appending given param x to the end of linked list.
        x - any type of class.
        Example of usages:
        ll1 = SingleLinkedList()
        for i in range(4):
            ll1.append(i)
        :param x:
        :return None:
        """

        if self.is_empty():
            self.head = Node(data=x)
            self.size += 1
            return

        tmp: Node = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = Node(data=x)
        self.size += 1

    def insert(self, pos: int, x: any) -> None:
        """
        Insert element at given index in list. List indexing starts with 0.
        Index may be negative.
        First param is index, second - element.
        Example of usages:
        ll1 = SingleLinkedList()
        ll1.insert(0, 1)
        :param pos:
        :param x:
        :return None:
        """
        if self.is_empty():
            self.head = Node(data=x)
            self.size += 1
            return

        is_negative_position: bool = pos < 0
        if pos == 0 or (is_negative_position and abs(pos) >= self.length()):
            self.head = Node(data=x, next=self.head)
            self.size += 1
            return

        elif pos >= self.length():
            tmp: Node = self.head
            while tmp.next:
                tmp = tmp.next
            tmp.next = Node(data=x)
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
        ll1 = SingleLinkedList()
        ll1.length()
        :return length of linked list:
        """
        return self.size

    def __len__(self) -> int:
        """
        Returning length of liked list.
        Use this for python builtin len() method.
        Time complexity O(1).
        Example of usages:
        ll1 = SingleLinkedList()
        len(ll1)
        :return length of linked list:
        """
        return self.length()

    def is_empty(self) -> bool:
        """
        Return true if linked list is empty, otherwise return False
        Example of usages:
        ll1 = SingleLinkedList()
        ll1.is_empty()
        :return boolean type True or False:
        """
        return self.length() == 0

    def contains(self, x: any) -> bool:
        """
        Returning true if element or Node exists in linked list nodes data, otherwise return false
        Example of usages:
        ll1 = SingleLinkedList()
        for i in range(4):
            ll1.append(i)
        x = ll1.head
        ll1.contains(x) or ll1.contains(0)
        :param x:
        :return boolean type of True and False:
        """
        if isinstance(x, Node) and self.contains_node(x):
            return self.contains_node(x)
        if self.is_empty():
            return False
        tmp: Node = self.head
        while tmp:
            if tmp.data == x or tmp.data is x:
                return True
            tmp = tmp.next
        return False

    def __contains__(self, x: any) -> bool:
        """
        Returning true if element or Node exists in linked list, otherwise return false.
        Use for builtin python "in" function.
        Example of usages:
        ll1 = SingleLinkedList()
        x = 5
        x in ll1
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
        ll1 = SingleLinkedList()
        x = Node(data=5)
        ll1.contains_node(x)
        :param x:
        :return boolean type of True and False:
        """
        if not isinstance(x, Node):
            raise ValueError(f"{type(x)} should be Node instance")
        if self.is_empty():
            return False
        tmp: Node = self.head
        while tmp:
            if tmp is x:
                return True
            tmp = tmp.next
        return False

    def pop(self) -> Node:
        """
        Deleting last element in linked list.
        Raise ValueError if list is empty.
        Example of usages:
        ll1 = SingleLinkedList()
        ll1.append(1)
        ll1.pop()
        :return data of object Node instance:
        """
        if self.is_empty():
            raise IndexError("Can't delete from empty linked list")
        if self.length() == 1:
            val: Node = self.head
            self.head = None
            self.size -= 1
            return val
        tmp: Node = self.head
        while tmp.next.next:
            tmp = tmp.next
        val: Node = tmp.next
        tmp.next = None
        self.size -= 1
        return val

    def remove(self, x: any) -> Node:
        """
        Remove first occurrences of given element/Node in list nodes data and return it Node instance.
        Example of usages:
        ll1 = SingleLinkedList()
        x = Node(data=5)
        ll1.append(x.data)
        ll1.remove(x.data)
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
            self.size -= 1
            return val
        if self.head.data == x or self.head.data is x:
            val: Node = self.head
            self.head = self.head.next
            self.size -= 1
            return val.data
        tmp: Node = self.head
        while tmp.next:
            if tmp.next.data == x or tmp.next.data is x:
                val: Node = tmp.next
                tmp.next = tmp.next.next
                self.size -= 1
                return val.data
            tmp = tmp.next

    def remove_node(self, x: Node) -> Node:
        """
        Remove given Node instance from linked list and return it.
        Example of usages:
        ll1 = SingleLinkedList()
        x = Node(data=1)
        ll1.append(x.data)
        ll1.remove_node(x)
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
            self.size -= 1
            return val
        if self.head is x:
            val: Node = self.head
            self.head = self.head.next
            self.size -= 1
            return val
        tmp: Node = self.head
        while tmp.next:
            if tmp.next is x:
                val: Node = tmp.next
                tmp.next = tmp.next.next
                self.size -= 1
                return val
            tmp = tmp.next

    def remove_at(self, x: int) -> Node:
        """
        Removing Node at given position. Indexing of linked list starts with 1.
        Example of usages:
        ll1 = SingleLinkedList()
        for i in range(10):
            ll1.append(i)
        ll1.remove_at(10)
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
        ll1 = SingleLinkedList()
        for i in range(5):
            ll1.append(i)
        ll1.reverse()
        :return None:
        """
        if self.is_empty():
            raise ValueError("Can't reverse empty linked list")
        prev: Node | None = None
        current: Node = self.head
        while current:
            nxt: Node = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def clear(self) -> None:
        """
        Clear all elements in linked list.
        Time complexity O(1).
        Example of usages:
        ll1 = SingleLinkedList()
        for i in range(10):
            ll1.append(i)
        ll1.clear()
        :return None:
        """
        self.head = None
        self.size = 0


# TODO DoubleLinkedList, CircularLinkedList
class DoubleLinkedList:
    """
    Implementation of Double Linked List.
    To see all available methods call all_methods method.
    Example of usages:
    dll1 = DoubleLinkedList()
    ddl1.all_methods()
    """
    def __init__(self, head: DoubleNode | None = None):
        self.head: DoubleNode | None = head
        self.tail: DoubleNode | None = self.head
        self.size: int = 0

    def __str__(self) -> str:
        """
        Returning string representation of double linked list in follow way:
        None<->Value_of_Node<->Value_of_Node<->...<->None
        :return str
        """
        if self.is_empty():
            return 'None'
        output: list[str] = ['None']
        tmp: DoubleNode = self.head
        while tmp:
            output.append(str(tmp))
            tmp = tmp.next
        output.append('None')
        return '<->'.join(output)

    def all_methods(self) -> list[str]:
        """
        Returning list name of all available methods.
        :return list of strings:
        """
        return dir(DoubleLinkedList)

    def append(self, x: any) -> None:
        """
        Appending given param x to the end of double linked list.
        x - any type of class.
        Example of usages:
        dll1 = DoubleLinkedList()
        for i in range(3):
            dll1.append(i)
        :param x:
        :return None:
        """
        if self.is_empty():
            self.head = DoubleNode(data=x, prev=None, next=None)
            self.size += 1
            self.tail = self.head
            return
        self.tail.next = DoubleNode(data=x, prev=self.tail)
        self.tail = self.tail.next
        self.size += 1

    def prepend(self, x: any) -> None:
        """
        Appending given element to the head of double linked list.
        Exmaple of usages:
        dll1 = DoubleLinkedList()
        for i in range(2):
            dll1.prepend(i)
        :param x:
        :return None:
        """
        if self.is_empty():
            self.head = DoubleNode(data=x)
            self.tail = self.head
            self.size += 1
            return
        self.head.prev = DoubleNode(data=x, next=self.head)
        self.head = self.head.prev
        self.size += 1

    def insert(self, pos: int, x: any) -> None:
        """
        Insert element at given index in list. List indexing starts with 0.
        Index may be negative.
        First param is index, second - element.
        Example of usages:
        dll1 = DoubleLinkedList()
        dll1.insert(0, 1)
        :param pos:
        :param x:
        :return None:
        """
        if self.is_empty():
            self.head = DoubleNode(data=x)
            self.size += 1
            self.tail = self.head
            return

        is_negative_position: bool = pos < 0
        if pos == 0 or (is_negative_position and abs(pos) >= self.length()):
            new: DoubleNode = DoubleNode(data=x, next=self.head)
            self.head.prev = new
            self.head = new
            self.size += 1
            return

        elif pos >= self.length():
            self.tail.next = DoubleNode(data=x, prev=self.tail,)
            self.tail = self.tail.next
            self.size += 1
            return

        if is_negative_position:
            pos = self.length() - abs(pos)

        idx: int = 0
        tmp: DoubleNode = self.head
        while idx < pos:
            idx += 1
            tmp = tmp.next
        new: DoubleNode = DoubleNode(data=x, prev=tmp.prev, next=tmp)
        tmp.prev.next = new
        tmp.prev = new
        self.size += 1

    def length(self) -> int:
        """
        Returning length of double linked list.
        Time complexity O(1).
        Example usages:
        dll1 = DoubleLinkedList()
        dll1.length()
        :return int - length of double linked list:
        """
        return self.size

    def __len__(self) -> int:
        """
        Returning length of double liked list.
        Use this for python builtin len() method.
        Time complexity O(1).
        Example of usages:
        dll1 = DoubleLinkedList()
        len(dll1)
        :return int - length of double linked list:
        """
        return self.length()

    def is_empty(self) -> bool:
        """
        Return true if double linked list is empty, otherwise return False
        Example of usages:
        dll1 = DoubleLinkedList()
        dll1.is_empty()
        :return boolean type True or False:
        """
        return self.length() == 0

    def contains(self, x: any) -> bool:
        """
        Return true if element or DoubleNode instance exist in linked list nodes data.
        Example of usages:
        dll1 = DoubleLinkedList()
        for i in range(1, 11):
            dll1.append(i)
        x = dll1.head
        dll1.contains(x) or dll1.contains(1)
        :param x:
        :return Boolean type of True and False:
        """
        if isinstance(x, DoubleNode) and self.contains_node(x):
            return self.contains_node(x)
        if self.is_empty():
            return False
        tmp: DoubleNode = self.head
        while tmp:
            if tmp.data == x or tmp.data is x:
                return True
            tmp = tmp.next
        return False

    def __contains__(self, x: any) -> bool:
        """
        Return true if element or Double node exist in linked list.
        Use for python builtin "in" method.
        Example of usages:
        dll1 = DoubleLinkedList()
        for i in range(3):
            dll1.append(i)
        1 in dll1
        :param x:
        :return boolean true of false:
        """
        if isinstance(x, DoubleNode) and self.contains_node(x):
            return self.contains_node(x)
        return self.contains(x)

    def contains_node(self, x: any) -> bool:
        """
        Return true if Double Node instance is one of the linked list nodes, otherwise return false.
        Example of usages:
        dll1 = DoubleLinkedList()
        for i in range(2):
            dll1.append(i)
        x = dll1.head.next
        dll1.contains_node(x)
        :param x:
        :return boolean true or false:
        """
        if not isinstance(x, DoubleNode):
            raise ValueError(f"Element= {x} Shoul be DoubleNode instance")
        if self.is_empty():
            return False
        tmp: DoubleNode = self.head
        while tmp:
            if tmp is x:
                return True
            tmp = tmp.next
        return False

    def pop(self) -> DoubleNode:
        """
        Remove from tail(rightmost) element and returning it.
        Example of usages:
        dll1 = DoubleLinkedList()
        for i in range(4):
            dll1.append(i)
        dll1.pop()
        :return data of DoubleNode instance:
        """
        if self.is_empty():
            raise IndexError("Can't delete from empty list")
        if self.length() == 1:
            val: DoubleNode = self.head
            self.head = None
            self.tail = self.tail
            self.size -= 1
            return val.data
        val: DoubleNode = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1
        return val.data

    def popleft(self) -> DoubleNode:
        """
        Removing from head(leftmost) node and return it.
        Example of usages:
        dll1 = DoubleLinkedList()
        for i in range(2):
            dll1.append(i)
        dll1.popleft()
        :return data of Double Node instance:
        """
        if self.is_empty():
            raise IndexError("Can't remove from empty list")
        if self.length() == 1:
            val: DoubleNode = self.head
            self.head = None
            self.tail = self.head
            self.size -= 1
            return val.data
        val: DoubleNode = self.head
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1
        return val.data

    def remove(self, x: any) -> DoubleNode:
        """
        Remove given element or DoubleNode if it exists in list nodes data and return it.
        Example of usages:
        dll1 = DoubleLinkedList()
        for i in range(2):
            dll1.append(i)
        dll1.remove(1)
        :param x:
        :return data of DoubleNode instance:
        """
        if self.is_empty():
            raise IndexError("Can't delete from empty list")
        if isinstance(x, DoubleNode) and self.contains_node(x):
            return self.remove_node(x)
        if not self.contains(x):
            raise ValueError(f"Element= {x} not in list")

        if self.length() == 1:
            val: DoubleNode = self.head
            self.head = None
            self.tail = self.head
            self.size -= 1
            return val.data

        tmp: DoubleNode = self.head
        while tmp:
            if tmp.data == x or tmp.data is x:
                if tmp is self.tail:
                    val: DoubleNode = tmp
                    self.tail = tmp.prev
                    self.tail.next = tmp.next
                    self.size -= 1
                    return val.data

                elif tmp is self.head:
                    val: DoubleNode = tmp
                    self.head = tmp.next
                    self.head.prev = None
                    self.size -= 1
                    return val.data

                val: DoubleNode = tmp
                tmp.prev.next = tmp.next
                tmp.next.prev = tmp.prev
                self.size -= 1
                return val.data
            tmp = tmp.next

    def remove_node(self, x: DoubleNode) -> DoubleNode:
        """
        Delete given DoubleNode x if it is one of double nodes in list and return node.
        Example of usages:
        dll1 = DoubleLinkedList()
        for i in range(4):
            dll1.append(i)
        dll1.remove_node(dll1.head)
        :param x:
        :return instance of DoubleNode class:
        """
        if not isinstance(x, DoubleNode):
            raise ValueError(f"{type(x)} should be DoubleNode instance")
        if self.is_empty():
            raise IndexError("Can't delete from emtpy list")
        if not self.contains_node(x):
            raise ValueError(f"Node {x} not in list nodes")
        if self.length() == 1:
            val: DoubleNode = self.head
            self.head = None
            self.tail = self.head
            self.size -= 1
            return val.data

        tmp: DoubleNode = self.head
        while tmp:
            if tmp is x:
                if tmp is self.tail:
                    val: DoubleNode = tmp
                    self.tail = tmp.prev
                    tmp.prev.next = tmp.next
                    self.size -= 1
                    return val

                elif tmp is self.head:
                    val: DoubleNode = tmp
                    self.head = tmp.next
                    self.head.prev = None
                    self.size -= 1
                    return val

                val: DoubleNode = tmp
                tmp.prev.next = tmp.next
                tmp.next.prev = tmp.prev
                self.size -= 1
                return val
            tmp = tmp.next

    def remove_at(self, x: int) -> DoubleNode:
        """
        Deleting node at given position. 1 indexing of list.
        Example of usages:
        dll1 = DoubleLinkedList()
        for i in range(5):
            dll1.append(i)
        dll1.remove_at(1)
        :param x:
        :return instance of DoubleNode class:
        """
        if self.is_empty():
            raise IndexError("Can't delete from empty list")
        if not 1 <= x <= self.length():
            raise IndexError(f"List index= {x} out of range")
        idx: int = 1
        tmp: DoubleNode = self.head
        while idx < x:
            idx += 1
            tmp = tmp.next
        return self.remove_node(tmp)

    def reverse(self) -> None:
        """
        Reversing linked list. Time Complexity is O(N) and Memory Complexity is O(1).
        Example of usages:
        dll1 = DoubleLinkedList()
        for i in range(5):
            dll1.append(i)
        dll1.reverse()
        :return None:
        """
        if self.is_empty():
            raise ValueError("Can't reverse empty linked list")

        current: DoubleNode = self.head
        prev_node: DoubleNode | None = None
        while current:
            next_node: DoubleNode = current.next
            current.next = prev_node
            current.prev = next_node
            prev_node = current
            current = next_node
        self.head = prev_node

    def clear(self) -> None:
        """
        Clear all elements in linked list.
        Time complexity O(1).
        Example of usages:
        dll1 = DoubleLinkedList()
        for i in range(10):
            dll1.append(i)
        dll1.clear()
        :return None:
        """
        self.head = None
        self.tail = self.head
        self.size = 0
