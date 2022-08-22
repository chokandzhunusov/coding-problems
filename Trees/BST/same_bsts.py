"""
Time complexity: O(n^2) For searching values smaller/greater. Even if it shrinks in size.
Space complexity: O(n^2)
"""

from typing import Optional


class BST:
    def __init__(self, value: 'int', left: 'Optional[BST]' = None, right: 'Optional[BST]' = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def get_smaller(array: 'list[int]') -> 'list[int]':
    smaller_numbers = []
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller_numbers.append(array[i])
    return smaller_numbers


def get_bigger_or_equal(array: 'list[int]') -> 'list[int]':
    bigger_numbers = []
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            bigger_numbers.append(array[i])
    return bigger_numbers


def same_BSTs(array_one: 'list[int]', array_two: 'list[int]'):
    if len(array_one) != len(array_two):
        return False

    if not array_one and not array_two:
        return True
    
    if array_one[0] != array_two[0]:
        return False
    
    left_one = get_smaller(array_one)
    left_two = get_smaller(array_two)

    right_one = get_bigger_or_equal(array_one)
    right_two = get_bigger_or_equal(array_two)

    return same_BSTs(left_one, left_two) and same_BSTs(right_one, right_two)


def main() -> None:    
    array_one = [10, 15, 8, 12, 94, 81, 5, 2, 11]
    array_two = [10, 8, 5, 15, 2, 12, 11, 94, 81]
    ans = same_BSTs(array_one, array_two)
    print(f'The ans is: {ans}')
    

if __name__ == '__main__':
    main()
