class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(list_repr: str) -> Node | None:
    values = list_repr.split(' -> ')[:-1]
    for ind, val in enumerate(values):
        try:
            integer = int(val)
            values[ind] = integer
        except ValueError:
            pass
    latest_node = Node(values[-1], None)
    values = values[:-1][::-1]
    for val in values:
        latest_node = Node(val, latest_node)

    return latest_node
