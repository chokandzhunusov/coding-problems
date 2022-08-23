"""
Time complexity: 
    - Recursive: O(logn)
    - Iterative: O(logn)
Space complexity: O()
    - Recursive: O(logn)
    - Iterative: O(1)
"""


def recursive_binary_search(array: 'list[int]', target: 'int', left_idx: 'int', right_idx: 'int'):
    if left_idx >= right_idx:
        return -1
    
    mid_idx = (left_idx + right_idx) // 2

    if target == array[mid_idx]:
        return mid_idx
    elif target < array[mid_idx]:
        return recursive_binary_search(array, target, left_idx, mid_idx-1)
    elif target > array[mid_idx]:
        return recursive_binary_search(array, target, mid_idx+1, right_idx)

    return -1


def iterative_binary_search(array: 'list[int]', target: 'int', left_idx: 'int', right_idx: 'int'):
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if target == array[mid_idx]:
            return mid_idx
        elif target < array[mid_idx]:
            right_idx = mid_idx - 1
        elif target > array[mid_idx]:
            left_idx = mid_idx + 1

    return -1


def main() -> None:    
    # array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    array = [1, 5, 23, 111]
    target = 23
    
    left_idx = 0
    right_idx = len(array) - 1
    
    ans = recursive_binary_search(array, target, left_idx, right_idx)
    
    print(f'The ans is: {ans}')
    

if __name__ == '__main__':
    main()
