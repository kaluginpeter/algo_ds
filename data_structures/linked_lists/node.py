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
        return f"'{self.data}'" if type(self.data) == str else f'{self.data}'
