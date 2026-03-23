class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    current = head
    while current is not None and current.next is not None:
        next_node = current.next
        current_node = current
        following_pair = next_node.next
        next_node.next = current_node
        current_node.next = following_pair
    return head
