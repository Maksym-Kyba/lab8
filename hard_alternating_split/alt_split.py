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
    first_list = Node(None)
    previous_first_list = current.data
    second_list = Node(None)
    previous_second_list = current.next.data
    current = current.next.next
    while current is not None and current.next is not None:
        change_list += 1
        if change_list % 2 == 1:
            first_list.data = previous_first_list
            first_list.next = current.next.data
            previous_first_list = first_list
        if change_list % 2 == 0:
            second_list.data = previous_second_list
            second_list.next = current.next.data
            previous_second_list = second_list
        current = current.next

    first_list.data = previous_first_list
    first_list.next = None
    second_list.data = previous_second_list
    second_list.next = None

    return Context(first_list, second_list)
