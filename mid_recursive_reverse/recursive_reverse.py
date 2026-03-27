class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    if head is None:
        return None

    def node_list(node):
        if node.next is None:
            return [node]
        return [node] + node_list(node.next)

    my_nodes = node_list(head)[::-1]
    start = my_nodes[0]
    for ind, node in enumerate(my_nodes):
        try:
            node.next = my_nodes[ind + 1]
        except IndexError:
            node.next = None

    return start
