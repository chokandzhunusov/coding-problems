"""
Time complexity: O(n)
Space complexity: O(1) 

1st pointer took to meet 2nd pointer: X distance
2nd pointer took to meet 1st pointer: 2X distance

Distance till the loop: D
Distance from start of loop to point where 1st and 2nd pointers met: P

From where 1st and 2nd pointers met till start of loop: R

Total Distance = Distance Travelled 2nd pointer - P
               = 2D + 2P - P
               = 2D + P

R = T - P - D
  = 2D + P - P - D
  = D
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


def find_loop(head_node: 'Node') -> 'Node':
    node_1 = head_node.next
    node_2 = head_node.next.next

    while node_1 != node_2:
        node_1 = node_1.next
        node_2 = node_2.next.next

    node_1 = head_node
    while node_1 != node_2:
        node_1 = node_1.next
        node_2 = node_2.next
    
    return node_1


def main() -> None:
    node_1 = Node(0)
    node_2 = Node(1, node_1)
    node_3 = Node(2, node_2)
    node_4 = Node(3, node_3)
    node_5 = Node(4, node_4)
    node_6 = Node(5, node_5)
    node_7 = Node(6, node_6)
    node_8 = Node(7, node_7)
    node_9 = Node(8, node_8)
    node_10 = Node(9, node_9)

    node_1.next = node_5

    LL = LinkedList() 
    LL.head = node_10
    head_node = LL.head
    ans = find_loop(head_node)
    print(ans.value)
    # while head_node:
    #     print(f'{head_node.value} -> ', end="")
    #     head_node = head_node.next


if __name__ == '__main__':
    main()
