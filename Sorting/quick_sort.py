"""
Time complexity: O(nlog(n)) for best and average. O(n^2) in worst case.
Space complexity: O(nlog(n))
"""


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def quick_sort(array: 'list[int]', start_idx: 'int', end_idx: 'int') -> 'list[int]':
    if start_idx >= end_idx:
        return array
    
    pivot_idx = start_idx
    left_idx = start_idx + 1
    right_idx = end_idx

    while right_idx >= left_idx:
        if array[left_idx] > array[pivot_idx] and array[right_idx] < array[pivot_idx]:
            swap(left_idx, right_idx, array)
        if array[left_idx] <= array[pivot_idx]:
            left_idx += 1
        if array[right_idx] >= array[pivot_idx]:
            right_idx -= 1
        
    swap(pivot_idx, right_idx, array)
    left_subarray_smaller = right_idx - 1 - start_idx < end_idx - (right_idx + 1)

    # The folowing idea is to first check the smaller subarray.
    if left_subarray_smaller:
        quick_sort(array, start_idx, right_idx - 1)
        quick_sort(array, right_idx + 1, end_idx)
    else:
        quick_sort(array, right_idx + 1, end_idx)
        quick_sort(array, start_idx, right_idx - 1)
    
    return array
    

def main() -> None:
    array = [8, 5, 2, 9, 5, 6, 3]
    ans = quick_sort(array, 0, len(array)-1)

    print(f'The ans is: {ans}')


if __name__ == '__main__':
    main()
