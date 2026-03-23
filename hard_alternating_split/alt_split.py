class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    current = head
    change_list = 0
    if current is None or current.next is None:
        raise IndexError
    first_list_start = Node(None)
    first_list = first_list_start
    second_list_start = Node(None)
    second_list = second_list_start
    while current is not None:
        change_list += 1
        if change_list % 2 == 1:
            new_node = Node(current.data)
            first_list.next = new_node
            first_list = new_node
        if change_list % 2 == 0:
            new_node = Node(current.data)
            second_list.next = new_node
            second_list = new_node
        current = current.next

    return Context(first_list_start.next, second_list_start.next)
