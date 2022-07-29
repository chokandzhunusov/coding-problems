"""
Time complexity: O(n^2) loops(for, while).
Space complexity: O(n) for storing array of tripplets.
"""


def three_number_sum(array: 'list[int]', target_sum: 'int') -> 'list[list[int]]':
    array.sort()
    tripplets = []
    for (i, num_1) in enumerate(array):
        left_number_index = i + 1
        right_number_index = len(array) - 1
        while left_number_index < right_number_index:
            tripplet_to_compare = num_1 + array[left_number_index] + array[right_number_index]
            if tripplet_to_compare == target_sum:
                tripplets.append([num_1, array[left_number_index], array[right_number_index]])
                left_number_index += 1
                right_number_index -= 1
            elif tripplet_to_compare < target_sum:
                left_number_index += 1
            elif tripplet_to_compare > target_sum:
                right_number_index -= 1
    return tripplets


def main() -> None:
    ans = three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0)
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
