"""
Time complexity: O(n+m)
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


def merge_ll(head_node_1: 'Node', head_node_2: 'Node') -> 'Node':
    p1 = head_node_1
    p2 = head_node_2
    temp = None

    while p1 is not None and p2 is not None:
        if p1.value < p2.value:
            temp = p1
            p1 = p1.next
        else:
            if temp is not None:
                temp.next = p2
            temp = p2
            p2 = p2.next
            temp.next = p1
    if p1 is None:
        temp.next = p2

    return head_node_1 if head_node_1.value < head_node_2.value else head_node_2
    
    
def main() -> None:
    node_2 = Node(10)
    node_3 = Node(9, node_2)
    
    node_4 = Node(5, node_3)
    node_5 = Node(3, node_4)
    node_6 = Node(1, node_5)

    node_7 = Node(8)
    node_8 = Node(7, node_7)
    node_9 = Node(6, node_8)
    node_10 = Node(2, node_9)

    LL = LinkedList() 
    LL.head = node_6
    head_node_1 = LL.head

    LL2 = LinkedList() 
    LL2.head = node_10
    head_node_2 = LL2.head
    
    result_node = merge_ll(head_node_1, head_node_2)

    while result_node:
        print(f'{result_node.value} -> ', end="")
        result_node = result_node.next


if __name__ == '__main__':
    main()
