class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    current = head
    prev_head = Node(None)
    prev_head.next = head
    previous = prev_head
    while current is not None and current.next is not None:
        if current.data != current.next.data:
            previous = current
            current = current.next
            continue
        value = current.data
        while current.next is not None and current.next.data == value:
            current = current.next
        previous.next = current

    return prev_head.next
