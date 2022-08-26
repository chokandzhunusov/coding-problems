"""
Time complexity: O(n^2)
Space complexity: O(1)
"""

    
def selection_sort(array: 'list[int]') -> 'list[int]':
    current_idx = 0
    while current_idx < len(array) - 1:
        smallest_idx = current_idx
        for i in range(current_idx + 1, len(array)):
            if array[smallest_idx] > array[i]:
                smallest_idx = i
        array[current_idx], array[smallest_idx] = array[smallest_idx], array[current_idx]
        current_idx += 1
    return array


def main() -> None:
    array = [8, 5, 2, 9, 5, 6, 3]
    ans = selection_sort(array)

    print(f'The ans is: {ans}')


if __name__ == '__main__':
    main()
