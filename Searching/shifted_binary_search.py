"""
Time complexity: O(log(n))
Space complexity: O(1)
"""


def helper(array: 'list[int]', target: 'int', left_idx, right_idx: 'int'):
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        potential_match = array[mid_idx]
        
        left_num = array[left_idx]
        right_num = array[right_idx]

        if target == potential_match:
            return mid_idx
        elif left_num <= potential_match:
            if target < potential_match and target >= left_num:
                right_idx = mid_idx - 1
            else:
                left_idx = mid_idx + 1
        else:
            if target > potential_match and target <= right_num:
                left_idx = mid_idx + 1
            else:
                right_idx = mid_idx - 1
    return -1
    

def shifted_binary_search(array: 'list[int]', target: 'int'):
    return helper(array, target, 0, len(array)-1)


# def get_number_of_shifted_indices(array: 'list[int]'):
#     for idx in range(len(array) - 1):
#         current = array[idx]
#         next = array[idx + 1]
#         if next < current:
#             return idx + 1
#     return 0


# def get_left_and_right_indices(array: 'list[int]', target: 'int'):
#     if array[0] == 0:
#         left_idx = 0
#         right_idx = len(array) - 1
#     else:
#         shifted_by = get_number_of_shifted_indices(array)
#         if target < array[0]:
#             left_idx = shifted_by
#             right_idx = len(array) - 1
#         else:
#             left_idx = 0
#             right_idx = shifted_by
    
#     return left_idx, right_idx


# def shifted_binary_search(array: 'list[int]', target: 'int'):
#     left_idx, right_idx = get_left_and_right_indices(array, target)

#     while left_idx <= right_idx:
#         mid_idx = (left_idx + right_idx) // 2
#         if target == array[mid_idx]:
#             return mid_idx
#         elif target < array[mid_idx]:
#             right_idx = mid_idx - 1
#         elif target > array[mid_idx]:
#             left_idx = mid_idx + 1

#     return -1


def main() -> None:    
    array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
    # array = [0, 1, 21, 33, 37, 45, 61, 71, 72, 73]
    target = 37
    
    ans = shifted_binary_search(array, target)
    
    print(f'The ans is: {ans}')
    

if __name__ == '__main__':
    main()
