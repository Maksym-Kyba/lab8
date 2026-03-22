class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    if not isinstance(node, Node):
        return 'None'
    result = ''
    while node.next is not None:
        result += f'{node.data} -> '
        node = node.next

    result += f'{node.data} -> None'
    return result

