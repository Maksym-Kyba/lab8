class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    if head.next is None:
        
    head = head.next

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

def stringify(node):
    if not isinstance(node, Node):
        return 'None'
    result = ''
    while node.next is not None:
        result += f'{node.data} -> '
        node = node.next

    result += f'{node.data} -> None'
    return result

print(stringify(reverse(build_one_two_three())))
