class Node(object):
    def __init__(self):
        self.next = None

def loop_size(node):
    current_fast = node
    current_slow = node
    starting_node = node
    size = 1

    meeting_checker = 0
    while current_fast is not None:
        if meeting_checker == 0:
            current_fast = current_fast.next.next
            current_slow = current_slow.next

        elif meeting_checker == 1:
            current_fast = current_fast.next
            current_slow = current_slow.next

        if current_fast == current_slow:
            current_slow = starting_node
            meeting_checker += 1


        if meeting_checker == 2:
            cycle_start = current_fast
            break

    current = cycle_start
    while current.next != cycle_start:
        size += 1
        current = current.next

    return size
