"""
Time complexity: O(n)
Space complexity: O(n)
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head):
        self.head = head


def remove_duplicates(linked_list_head: "LinkedList") -> "LinkedList":
    current_node = linked_list_head
    while current_node is not None:
        distinct_node = current_node.next
        while distinct_node is not None and current_node.value == distinct_node.value:
            distinct_node = distinct_node.next
        current_node.next = distinct_node
        current_node = distinct_node
    return linked_list_head   


def main() -> None:
    node_8 = Node(6)
    node_7 = Node(6, next=node_8)
    node_6 = Node(5, next=node_7)
    node_5 = Node(4, next=node_6)
    node_4 = Node(4, next=node_5)
    node_3 = Node(3, next=node_4)
    node_2 = Node(1, next=node_3)
    node_1 = Node(1, next=node_2)
    head = Node(1, next=node_1)
    LList = LinkedList(head)
    
    remove_duplicates(LList.head)
    
    temp = head
    while temp:
        print(f'{temp.value} -> ', end="")
        temp = temp.next


if __name__ == '__main__':
    main()
