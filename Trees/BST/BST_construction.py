"""
Time complexity: O(log(n)) 
Space complexity: O(log(n))
"""

from typing import Optional


class BST:
    def __init__(self, value: 'int', left: 'Optional[BST]' = None, right: 'Optional[BST]' = None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

    def contains(self, value):
        if value < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(value)
        elif value > self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(value)
        else:
            return True
        
    def remove(self, value, parent=None):
        if value < self.value:
            if self.left:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right:
                self.right.remove(value, self)
        else:
            if self.left and self.right:
                self.value = self.right.get_min_value()
                self.right.remove(self.value, self)
            elif not parent:
                if self.left:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                
                elif self.right:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    pass  # Single node tree, do nothing.
            elif parent.left == self:
                parent.left = self.left if self.left else self.right
        
            elif parent.right == self:
                parent.right = self.left if self.left else self.right
        return self

    def get_min_value(self):
        if not self.left:
            return self.value
        else:
            return self.left.get_min_value()

    def show(self):
        queue = [self]
        result = []
        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        print(result)


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
    tree.contains(15)
    tree.show()

    new = tree.remove(5)
    new.show()

    

if __name__ == '__main__':
    main()
