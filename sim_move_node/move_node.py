class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    node_to_add = source.data
    source = source.next
    dest_new = Node(node_to_add)
    dest_new.next = dest
    return Context(source, dest_new)
