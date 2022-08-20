"""
Time complexity: O(n) 
Space complexity: O(n)
"""

from typing import Optional


class BST:
    def __init__(self, value: 'int', left: 'Optional[BST]' = None, right: 'Optional[BST]' = None):
        self.value = value
        self.left = left
        self.right = right


def construct_min_height_BST(array: 'list[int]', start_index: 'int', end_index: 'int'):
    if end_index < start_index:
        return None
    mid_index = (start_index + end_index) // 2
    bst = BST(array[mid_index])
    bst.left = construct_min_height_BST(array, start_index, mid_index - 1)
    bst.right = construct_min_height_BST(array, mid_index + 1, end_index)
    return bst
    

def min_height_BST(array: 'list[int]') -> 'BST':
    return construct_min_height_BST(array, 0, len(array) - 1)   
    

def show(node: 'BST', array: 'list'):
    if node:
        array.append(node.value)
        show(node.left, array)
        show(node.right, array)
    return array


def main() -> None:    
    root = min_height_BST([1, 2, 5, 7, 10, 13, 14, 15, 22])
    ans = show(root, [])
    print(f'The ans is: {ans}')
    

if __name__ == '__main__':
    main()
