class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def push(head, data):
    return Node(data, head)

def build_one_two_three():
    head = None
    num = 3
    while num != 0:
        head = push(head, num)
        num -= 1

    return head
