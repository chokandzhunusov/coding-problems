"""
Time complexity: O(h) height of tree.
Space complexity: O(1)
"""

from typing import Optional


class BST:
    def __init__(self, value: 'int', left: 'Optional[BST]' = None, right: 'Optional[BST]' = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def is_descendant(node, target):
    while node and node != target:
        node = node.left if target.value < node.value else node.right
    return node is target


def validate_three_nodes(n1: 'BST', n2: 'BST', n3: 'BST'):
    if is_descendant(n2, n1):
        return is_descendant(n3, n2)
    
    if is_descendant(n2, n3):
        return is_descendant(n1, n2)
    
    return False
    

def main() -> None:    
    n1 = BST(5)
    n1.left = BST(2)
    n1.left.left = BST(1)
    n1.left.left.left = BST(0)
    n1.left.right = BST(4)
    n1.left.right.left = BST(3)
    
    n1.right = BST(7)
    n1.right.left = BST(6)
    n1.right.right = BST(8)
    ans = validate_three_nodes(n1, n1.left, n1.left.right.left)
    # ans = validate_three_nodes(n1, n1.right.right, n1.left.right.left)
    print(f'The ans is: {ans}')
    

if __name__ == '__main__':
    main()
