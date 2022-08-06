"""
Time complexity: O(n)
Space complexity: O(1)
"""

from typing import Optional


class Node:
    def __init__(self, value: 'int', next: Optional['Node'] = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head: Optional['Node'] = None, tail: Optional['Node'] = None):
        self.head = head
        self.tail = tail


def reverse(head_node: 'Node') -> 'Node':
    p1, p2 = None, head_node
    while p2 is not None:
        p3 = p2.next
        p2.next = p1
        p1 = p2
        p2 = p3

    return p1
    

def main() -> None:
    node_1 = Node(6)
    node_2 = Node(5, node_1)
    node_3 = Node(4, node_2)
    node_4 = Node(3, node_3)
    node_5 = Node(2, node_4)
    node_6 = Node(1, node_5)

    LL = LinkedList() 
    LL.head = node_6
    head_node = LL.head
    head_node = reverse(head_node)
    while head_node:
        print(f'{head_node.value} -> ', end="")
        head_node = head_node.next


if __name__ == '__main__':
    main()
