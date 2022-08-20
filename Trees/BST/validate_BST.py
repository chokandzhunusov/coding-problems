"""
Time complexity: O(n) 
Space complexity: O(d) depth of longest BST.
"""

from typing import Optional


class BST:
    def __init__(self, value: 'int', left: 'Optional[BST]' = None, right: 'Optional[BST]' = None):
        self.value = value
        self.left = left
        self.right = right


def validation_helper(tree: 'BST', min_value: 'int', max_value: 'int'):
    if not tree:
        return True  # Reached leaf node at current recursion stack
    if tree.value < min_value or tree.value >= max_value:
        return False
    left_is_valid = validation_helper(tree.left, min_value, tree.value)
    right_is_valid = validation_helper(tree.right, tree.value, max_value)
    return left_is_valid and right_is_valid
    

def validate_BST(tree: 'BST'):
    return validation_helper(tree, float('-inf'), float('inf'))
    

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
    
    ans = validate_BST(tree)

    print(f'The ans is: {ans}')
    

if __name__ == '__main__':
    main()
