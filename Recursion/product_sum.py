"""
Time complexity: O(n) including the elements in subarray.
Space complexity: O(d) for depth of nested arrays
"""


def product_sum(array: 'list[any]', depth=1):
    current_sum = 0
    for i in array:
        if isinstance(i, list):
            current_sum += product_sum(i, depth + 1)
        else:
            current_sum += i
    
    return depth * current_sum


def main() -> None:
    array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
    assert product_sum(array) == 12


if __name__ == '__main__':
    main()
