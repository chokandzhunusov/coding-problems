"""
Time complexity: O()
Space complexity: O()
"""

from operator import length_hint
from typing import Optional


class Node:
    def __init__(self, value: 'int', next: Optional['Node'] = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head: Optional['Node'] = None, tail: Optional['Node'] = None):
        self.head = head
        self.tail = tail


def remove_kth_node_from_end(head_node: 'Node', k: 'int') -> 'None':
    first = head_node
    second = head_node
    counter = 1

    while counter != k:
        second = second.next
        counter += 1

    if second is None:
        head_node.value = head_node.next.value
        head_node.next = head_node.next.next
        return

    while second is not None:
        first = first.next
        second = second.next
    
    first.next = first.next.next



def main() -> None:
    node_1 = Node(1)
    node_2 = Node(2, node_1)
    node_3 = Node(3, node_2)
    node_4 = Node(11, node_3)
    node_5 = Node(4, node_4)
    node_6 = Node(5, node_5)

    LL = LinkedList() 
    LL.head = node_6
    head_node = LL.head
    remove_kth_node_from_end(head_node, 6)
    while head_node:
        print(f'{head_node.value} -> ', end="")
        head_node = head_node.next


if __name__ == '__main__':
    main()
