"""
Time complexity: O(max(n, m)) max of first LL or second LL
Space complexity: O(max(n, m))
"""

from typing import Optional


class LinkedList:
    def __init__(self, value: 'int', next: Optional['any'] = None):
        self.value = value
        self.next = next


def sum_of_ll(ll_1, ll_2):
    new_ll_head_pointer = LinkedList(0)
    current_node = new_ll_head_pointer
    carry = 0

    n_one = ll_1
    n_two = ll_2

    while n_one or n_two or carry != 0:
        value_one = n_one.value if n_one else 0
        value_two = n_two.value if n_two else 0
        sum_of_values = value_one + value_two + carry

        new_value = sum_of_values % 10
        new_node = LinkedList(new_value)
        current_node.next = new_node
        current_node = new_node

        carry = sum_of_values // 10
        n_one = n_one.next if n_one else None
        n_two = n_two.next if n_two else None
    return new_ll_head_pointer.next


def main() -> None:
    n7 = LinkedList(5)
    n6 = LinkedList(4, n7)
    n5 = LinkedList(9, n6)

    n4 = LinkedList(1)
    n3 = LinkedList(7, n4)
    n2 = LinkedList(4, n3)
    n1 = LinkedList(2, n2)
    ans = sum_of_ll(n1, n5)
    
    while ans:
        print(ans.value, end=' => ')
        ans = ans.next


if __name__ == '__main__':
    main()