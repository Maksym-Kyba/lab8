class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    node_to_add = Node(data)
    if head is not None:
        if head.data > data:
            node_to_add.next = head
            return node_to_add

        head_copy = head
        while head_copy.next is not None:
            next_value = head_copy.next.data
            if next_value < data:
                head_copy = head_copy.next
                continue
            node_to_add.next = head_copy.next
            head_copy.next = node_to_add
            break
        else:
            node_to_add.next = head_copy.next
            head_copy.next = node_to_add
    else:
        head = Node(data)

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

print(stringify(build_one_two_three()))
print(stringify(sorted_insert(build_one_two_three(), 4)))
