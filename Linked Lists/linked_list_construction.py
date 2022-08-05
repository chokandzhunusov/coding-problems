"""
Time complexity: O()
Space complexity: O()
"""

from typing import Optional


class Node:
    def __init__(self, value: 'int', prev: Optional['Node'] = None, next: Optional['Node'] = None):
        self.value = value
        self.prev = next
        self.next = next


class DoublyLinkedList:
    def __init__(self, head: Optional['Node'] = None, tail: Optional['Node'] = None):
        self.head = head
        self.tail = tail

    def setHead(self, node: 'Node'):
        if not self.head:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)
        
    def setTail(self, node: 'Node'):
        if not self.tail:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)
      
    def insertBefore(self, node: 'Node', node_to_insert: 'Node'):
        if node_to_insert == self.head and node_to_insert == self.tail:
            return
        self.remove(node_to_insert)
        node_to_insert.prev = node.prev
        node_to_insert.next = node
        if not node.prev:
            self.head = node_to_insert
        else:
            node.prev.next = node_to_insert
        
        node.prev = node_to_insert
        
    def insertAfter(self, node: 'Node', node_to_insert: 'Node'):
        if node_to_insert == self.head and node_to_insert == self.tail:
            return

        self.remove(node_to_insert)
        node_to_insert.prev = node
        node_to_insert.next = node.next

        if not node.next:
            self.tail = node_to_insert
        else:
            node.next.prev = node_to_insert

        node.next = node_to_insert

    def insertAtPosition(self, position: 'int', node_to_insert: 'Node'):
        if position == 1:
            self.setHead(node_to_insert)
            return

        node = self.head
        current_position = 1
        while node is not None and current_position != position:
            node = node.next
            current_position += 1

        if node is not None:
            self.insertBefore(node, node_to_insert)
        else:
            self.setTail(node_to_insert)
    
    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            node_to_remove = node
            node = node.next
            if node_to_remove.value == value:
                self.remove(node_to_remove)
    
    def remove(self, node: 'Node'):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        
        node.prev = None
        node.next = None

    def containsNodeWithValue(self, value: 'int'):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None


def main() -> None:
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    DLL = DoublyLinkedList()
    DLL.setHead(node_1)
    DLL.insertAfter(node_1, node_2)
    DLL.insertBefore(node_1, node_3)
    
    head_node = DLL.head
    while head_node:
        print(f'{head_node.value} -> ', end="")
        head_node = head_node.next


if __name__ == '__main__':
    main()
