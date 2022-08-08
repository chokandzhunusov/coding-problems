"""
Time complexity: O(n^2)
Space complexity: O(n) storing recursive call stacks
"""


def insert_in_sorted_order(stack, value):
    if len(stack) == 0 or stack[len(stack)-1] <= value:
        stack.append(value)
        return

    peek = stack.pop()
    insert_in_sorted_order(stack, value)
    stack.append(peek)


def sort_stack(stack: 'list[int]') -> 'list[int]':
    if len(stack) == 0:
        return stack
        
    peek = stack.pop()
    sort_stack(stack)
    insert_in_sorted_order(stack, peek)
    return stack


def main() -> None:
    print(sort_stack([-5, 2, -2, 4, 3, 1]))


if __name__ == '__main__':
    main()