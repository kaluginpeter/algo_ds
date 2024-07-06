class DisjointSetUnion:
    """
    Implementation of Disjoint Set Union data sturcture.
    About Disjoint Set Union:
    What is a Disjoint set data structure?
    Two sets are called disjoint sets if they don’t have any element in common,
    the intersection of sets is a null set.
    A data structure that stores non overlapping or disjoint subset of elements is called disjoint set data structure.
    The disjoint set data structure supports following operations:
    Adding new sets to the disjoint set.
    Merging disjoint sets to a single disjoint set using Union operation.
    Finding representative of a disjoint set using Find operation.
    Check if two sets are disjoint or not.
    Consider a situation with a number of persons and the following tasks to be performed on them:
    Add a new friendship relation, i.e. a person x becomes the friend of another person y i.e adding new element to a set.
    Find whether individual x is a friend of individual y (direct or indirect friend)
    """
    def __init__(self, upper_boundary: int = None, sequence: iter = None) -> None:
        """
        Function that initialize disjoint set.
        :param upper_boundary: integer representing range of nodes, starting from 0 to n(not inclusive)
        :param sequence: iterable sequence. Disjoint set will automatically create set with this elements.
        """
        if upper_boundary:
            self.parents: list[int] = list(range(upper_boundary))
            self.ranks: list[int] = [1] * upper_boundary
            self.__connections: int = upper_boundary
        else:
            self.positions: dict[object, int] = {}
            index: int = 0
            for node in sequence:
                self.positions[node] = index
                index += 1
            self.parents: list[object] = list(sequence)
            self.ranks: list[int] = [1] * len(sequence)
            self.__connections: int = len(sequence)
        self.range_nodes: bool = bool(upper_boundary)

    def union(self, x: int, y: int) -> bool:
        """
        Function that connect(union) given nodes together.
        Return True if connections was successfully, otherwise return False,
        if connections between nodes already exists.
        :param x: Node of disjoint set
        :param y: Node of disjoint set
        :return: True if connection between node created and False if nodes already connected.
        Time Complexity O(Inverse Ackermann function(N)), that almost equal to O(1).
        Example of usages:
        dsu = DisjointSetUnion(3)
        dsu.union(0, 2) -> True
        dsu.union(2, 0) -> False
        """
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.ranks[(root_x if self.range_nodes else self.positions[root_x])] > self.ranks[(root_y if self.range_nodes else self.positions[root_y])]:
            self.parents[(root_y if self.range_nodes else self.positions[root_y])] = root_x
            self.ranks[(root_x if self.range_nodes else self.positions[root_x])] += 1
        elif self.ranks[(root_x if self.range_nodes else self.positions[root_x])] < self.ranks[(root_y if self.range_nodes else self.positions[root_y])]:
            self.parents[(root_x if self.range_nodes else self.positions[root_x])] = root_y
            self.ranks[(root_y if self.range_nodes else self.positions[root_y])] += 1
        else:
            self.parents[(root_y if self.range_nodes else self.positions[root_y])] = root_x
            self.ranks[(root_x if self.range_nodes else self.positions[root_x])] += 1
        self.__connections -= 1
        return True

    def find(self, x):
        """
        Function that find and return parent of given node.
        Time Complexity O(Inverse Ackermann function(N)), that almost equal to O(1).
        Example of Usages:
        dsu = DisjointSetUnion(3)
        dsu.find(2) -> 2
        dsu.union(0, 2) -> True
        dsu.find(2) -> 0
        :param x: Node of disjoint set
        :return: Parent of give node
        """
        root = x
        while root != self.parents[(root if self.range_nodes else self.positions[root])]:
            root =  self.parents[(root if self.range_nodes else self.positions[root])]
        while x != root:
            parent = self.parents[(x if self.range_nodes else self.positions[x])]
            self.parents[(x if self.range_nodes else self.positions[x])] = root
            x = parent
        return root

    def is_connected(self) -> bool:
        """
        Function that check if all nodes in disjoint set connected together.
        If it is, function return True and False otherwise.
        Time Complexity O(1).
        Example of Usages:
        dsu = DisjointSetUnion(3)
        dsu.is_connected() -> False
        for node in range(1, 3):
            dsu.union(0, node) -> True
        dsu.is_connected() -> True
        :return: boolean True of False
        """
        return self.__connections == 1

    def __str__(self) -> str:
        """
        Function that return object in his string representation. In next format:
        "
        Parents: node0: parentN, node1: parentN, ...
        Ranks: node0: rank0, node1: rank1, ...
        "
        Time Complexity O(N).
        Example of Usages:
        dsu = DisjointSetUnion(3)
        print(dsu) -> Parents: {0: 0, 1: 1, 2: 2}
                      Ranks: {0: 1, 1: 1, 2: 1}
        :return: string representation of object
        """
        if self.range_nodes:
            parents = ', '.join(f'{node}: {parent}' for node, parent in enumerate(self.parents))
            ranks = ', '.join(f'{node}: {rank}' for node, rank in enumerate(self.ranks))
        else:
            parents = ', '.join(f'{node}: {self.parents[self.positions[node]]}' for node in self.positions.keys())
            ranks = ', '.join(f'{node}: {self.ranks[self.positions[node]]}' for node in self.positions.keys())
        return f'Parents: {{{parents}}}\nRanks: {{{ranks}}}'

    def __repr__(self) -> str:
        """
        Function that return string representation of class/object. In next format:
        "
        Parents: node0: parentN, node1: parentN, ...\nRanks: node0: rank0, node1: rank1, ...
        "
        Time Complexity O(N).
        Example of Usages:
        dsu = DisjointSetUnion(3)
        repr(dsu) -> Parents: {0: 0, 1: 1, 2: 2}\nRanks: {0: 1, 1: 1, 2: 1}
        :return: string representation of class/object.
        """
        return self.__str__()

    def all_methods(self) -> list[str]:
        """
        Function that return list of names available methods in class.
        Example of Usages:
        dsu = DisjointSetUnion(10)
        dsu.all_methods() -> list[str, str, ...]
        :return: list contains string representing names of available methods in class.
        """
        return dir(DisjointSetUnion)
