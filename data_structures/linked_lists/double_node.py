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
