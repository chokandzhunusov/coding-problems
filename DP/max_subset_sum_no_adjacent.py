"""
Time complexity: O(n)
Space complexity: O(1)
"""

def max_subset_sum_no_adjacent(array: list) -> int:
    if not array:
        return 0
    elif len(array) == 1:
        return array[0]
    second = array[0]
    first = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
    return first


def main() -> None:
    array = [75, 105, 120, 75, 90, 135]
    print(max_subset_sum_no_adjacent(array))
    return


if __name__ == '__main__':
    main()