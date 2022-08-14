"""
Time complexity: O()
Space complexity: O()
"""


class Node:
    def __init__(self) -> None:
        self.children = []
        self.value = ''
        self.parent_has_childs_left = len(self.children) - 1
    
    def depth_first_search(self, array: 'list') -> 'list[str]':
        array.append(self.value)
        for child in self.children:
            child.depth_first_search(array)
        return array

    def breadth_first_search(self, array: 'list') -> 'list[str]':
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.value)
            for child in current.children:
                queue.append(child)
        return array


def main() -> None:

    n8 = Node()
    n8.value = 'J'
    
    n7 = Node()
    n7.value = 'I'
    
    n6 = Node()
    n6.children = [n7, n8]
    n6.value = 'F'
    
    n5 = Node()
    n5.value = 'E'

    n4 = Node()
    n4.value = 'D'
    
    n3 = Node()
    n3.value = 'C'

    n2 = Node()
    n2.children = [n5, n6]
    n2.value = 'B'
    
    n1 = Node()
    n1.children = [n2, n3, n4]
    n1.value = 'A'

    ans = n1.breadth_first_search([])
    
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
