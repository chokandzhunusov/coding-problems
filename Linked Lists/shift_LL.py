"""
Time complexity: O(n)
Space complexity: O(1)
"""

from tkinter import N
from typing import Optional


class Node:
    def __init__(self, value: 'int', next: Optional['Node'] = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head: Optional['Node'] = None, tail: Optional['Node'] = None):
        self.head = head
        self.tail = tail


def shift_ll(head_node: 'Node', k: 'int') -> 'Node':
    length_of_ll = 1
    tail = head_node
    
    while tail.next is not None:
        tail = tail.next
        length_of_ll += 1

    # Calculate distance from head/tail
    offset = abs(k) % length_of_ll

    if offset == 0:
        return head_node

    # Put new tail from head/tail
    new_tail_pos = length_of_ll - offset if k > 0 else offset
    new_tail = head_node

    for i in range(1, new_tail_pos):
        new_tail = new_tail.next
    
    new_head = new_tail.next
    new_tail.next = None
    tail.next = head_node
    
    return new_head
    
    
def main() -> None:
    node_2 = Node(5)
    node_3 = Node(4, node_2)
    node_4 = Node(3, node_3)
    node_5 = Node(2, node_4)
    node_6 = Node(1, node_5)
    node_7 = Node(0, node_6)

    LL = LinkedList() 
    LL.head = node_7
    head_node_1 = LL.head

    result_node = shift_ll(head_node_1, 2)

    while result_node:
        print(f'{result_node.value} -> ', end="")
        result_node = result_node.next


if __name__ == '__main__':
    main()
