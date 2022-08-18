"""
Time complexity: 
    Recursive: O(log(n))
    Iterative: O(log(n))
Space complexity:
    Recursive: O(log(n))
    Iterative: O(n)
"""

from typing import Optional


class BST:
    def __init__(self, value: 'int', left: 'Optional[BST]' = None, right: 'Optional[BST]' = None):
        self.value = value
        self.left = left
        self.right = right


def BST_recursive_helper(tree: 'BST', target: 'int', closest: 'int'):
    if not tree:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return BST_recursive_helper(tree.left, target, closest)
    elif target > tree.value:
        return BST_recursive_helper(tree.right, target, closest)
    else:
        return closest
        

def recursive_find_closest_value_in_BST(tree: 'BST', target: 'int'):
    return BST_recursive_helper(tree, target, tree.value)    


def BST_iterative_helper(tree: 'BST', target: 'int', closest: 'int'):
    current_node = tree
    while current_node:
        if abs(target - closest) > abs(target - current_node.value):
            closest = current_node.value
        if target < current_node.value:
            current_node = current_node.left
        elif target > current_node.value:
            current_node = current_node.right
        else:
            break
    return closest


def iterative_find_closest_value_in_BST(tree: 'BST', target: 'int'):
    return BST_iterative_helper(tree, target, tree.value)    


def main() -> None:    
    n8 = BST(14)
    
    n7 = BST(22)
    n6 = BST(13, n8)
    
    n5 = BST(1)

    n4 = BST(5)
    n3 = BST(2, n5)
    
    n2 = BST(15, n6, n7)
    n1 = BST(5, n3, n4)
    tree = BST(10, n1, n2)

    ans = recursive_find_closest_value_in_BST(tree, 12)
    print(f'Answer is: {ans}')
    

if __name__ == '__main__':
    main()
