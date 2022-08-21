"""
Time complexity: O(h + k) h => height of tree. 
    - Imagine going down far right to find the largest value in BST. 
    - Then you have to get back to find k'th node.
Space complexity: O(h) for the stack that will will used for recursive calls.
"""

from typing import Optional


class BST:
    def __init__(self, value: 'int', left: 'Optional[BST]' = None, right: 'Optional[BST]' = None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, num_of_visited_nodes: 'int', latest_visited_node_value: 'int'):
        self.num_of_visited_nodes = num_of_visited_nodes
        self.latest_visited_node_value = latest_visited_node_value


def find_largest_kth_value_in_BST(root: 'BST', k: 'int'):
    tree_info = TreeInfo(0, -1)
    reversed_in_order_traverse(root, k, tree_info)
    return tree_info.latest_visited_node_value


def reversed_in_order_traverse(node: 'BST', k: 'int', tree_info: 'TreeInfo'):
    if node is None or tree_info.num_of_visited_nodes >= k:
        return

    reversed_in_order_traverse(node.right, k, tree_info)
    if tree_info.num_of_visited_nodes < k:
        tree_info.num_of_visited_nodes += 1
        tree_info.latest_visited_node_value = node.value
        reversed_in_order_traverse(node.left, k, tree_info)


def main() -> None:    
    root = BST(15)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.left.right = BST(3)
    root.left.right = BST(5)
    root.right = BST(20)
    root.right.left = BST(17)
    root.right.right = BST(22)
    k = 3
    
    ans = find_largest_kth_value_in_BST(root, k)
    print(f'The ans is: {ans}')
    

if __name__ == '__main__':
    main()
