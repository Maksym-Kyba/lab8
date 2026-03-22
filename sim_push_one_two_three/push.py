class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    chained = Node(data)
    chained.next = head
    return chained

def build_one_two_three():
    head = None
    num = 3
    while num != 0:
        head = push(head, num)
        num -= 1

    return head
