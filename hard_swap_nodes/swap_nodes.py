class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    current = head
    previous_pair = None
    if head is not None and head.next is not None:
        head = head.next
    while current is not None and current.next is not None:
        next_node = current.next
        following_pair = next_node.next
        next_node.next = current
        current.next = following_pair

        if previous_pair is not None:
            previous_pair.next = next_node
        previous_pair = current
        current = following_pair
    return head
