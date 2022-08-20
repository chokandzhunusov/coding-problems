"""
Time complexity: O() 
Space complexity: O()
"""

from typing import Optional


class BST:
    def __init__(self, value: 'int', left: 'Optional[BST]' = None, right: 'Optional[BST]' = None):
        self.value = value
        self.left = left
        self.right = right


def in_order_traverse(tree: 'BST', array: 'list'):
    if tree:
        in_order_traverse(tree.left, array)
        array.append(tree.value)
        in_order_traverse(tree.right, array)
    return array


def pre_order_traverse(tree: 'BST', array: 'list'):
    if tree:
        array.append(tree.value)
        in_order_traverse(tree.left, array)
        in_order_traverse(tree.right, array)
    return array


def post_order_traverse(tree: 'BST', array: 'list'):
    if tree:
        in_order_traverse(tree.left, array)
        array.append(tree.value)
        in_order_traverse(tree.right, array)
    return array


def main() -> None:    
    n7 = BST(22)
    
    n5 = BST(1)

    n4 = BST(5)
    n3 = BST(2, n5)
    
    n2 = BST(15, right=n7)
    n1 = BST(5, n3, n4)
    tree = BST(10, n1, n2)
    
    ans_in = in_order_traverse(tree, [])
    ans_pre = pre_order_traverse(tree, [])
    ans_post = post_order_traverse(tree, [])

    print(f'The ans is: {ans_in, ans_pre, ans_post}')
    

if __name__ == '__main__':
    main()
