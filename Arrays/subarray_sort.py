"""
Time complexity: O(n)
Space complexity: O(1)
"""
    

def is_out_of_order(index: 'int', num: 'int', array: 'list[int]'):
    if index == 0:
        return num > array[index + 1]
    elif index == len(array) - 1:
        return num < array[index - 1]
    return num < array[index - 1] or num > array[index + 1]
    

def subarray_sort(array: 'list[int]') -> 'list[int]':
    min_out_of_order = float('inf')
    max_out_of_order = float('-inf')
    
    for i in range(len(array)):
        num = array[i]
        if is_out_of_order(i, num, array):
            min_out_of_order = min(num, min_out_of_order)
            max_out_of_order = max(num, max_out_of_order)
    
    if min_out_of_order == float('inf'):
        return [-1, -1]

    sub_array_left_idx = 0
    while min_out_of_order >= array[sub_array_left_idx]:
        sub_array_left_idx += 1
    
    sub_array_right_idx = len(array) - 1
    while max_out_of_order <= array[sub_array_right_idx]:
        sub_array_right_idx -= 1

    return [sub_array_left_idx, sub_array_right_idx]


def main() -> None:
    ans = subarray_sort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
