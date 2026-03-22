class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    num = 0
    if index < 0 or isinstance(index, float):
        raise IndexError
    if not isinstance(node, Node):
        raise TypeError
    while num != index and node is not None:
        node = node.next
        num += 1
    if node is None:
        raise IndexError
    return node
