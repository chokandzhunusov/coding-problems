"""
Time complexity: O()
Space complexity: O()
"""


def altered_BS(array: 'list[int]', target: 'int', left_idx, right_idx, result: 'list[int]', go_left: 'bool'):
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        number_at_mid = array[mid_idx]
        if number_at_mid < target:
            left_idx += mid_idx + 1
        elif number_at_mid > target:
            right_idx = mid_idx - 1
        else:
            if go_left:
                if mid_idx == 0 or array[mid_idx - 1] != target:
                    result[0] = mid_idx
                    return
                else:
                    right_idx = mid_idx - 1
            else:
                if mid_idx == len(array) - 1 or array[mid_idx + 1] != target:
                    result[1] = mid_idx
                    return
                else:
                    left_idx = mid_idx + 1


def search_for_range(array: 'list[int]', target: 'int'):
    result = [-1, -1]
    altered_BS(array, target, 0, len(array) - 1, result, True)
    altered_BS(array, target, 0, len(array) - 1, result, False)
    return result

# class Bounds:
#     def __init__(self) -> None:
#         self.far_left_idx = -1
#         self.far_right_idx = -1


# def helper(array: 'list[int]', target: 'int', left_idx: 'int', right_idx: 'int', bounds: 'Bounds'):
#     if left_idx > right_idx:
#         return

#     mid_idx = (left_idx + right_idx) // 2

#     if array[mid_idx] == target:
#         if bounds.far_left_idx < 0 or mid_idx < bounds.far_left_idx:
#             bounds.far_left_idx = mid_idx

#         if bounds.far_right_idx < 0 or mid_idx > bounds.far_right_idx:
#             bounds.far_right_idx = mid_idx
        
#     helper(array, target, left_idx, mid_idx - 1, bounds)
#     helper(array, target, mid_idx + 1, right_idx, bounds)
    
#     return [bounds.far_left_idx, bounds.far_right_idx]
            

# def search_for_range(array: 'list[int]', target: 'int'):
#     left_idx = 0
#     right_idx = len(array) - 1

#     bounds = Bounds()
    
#     return helper(array, target, left_idx, right_idx, bounds)
    

def main() -> None:    
    array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
    # array = [5, 7, 7, 8, 8, 10]
    target = 45
    ans = search_for_range(array, target)
    
    print(f'The ans is: {ans}')
    

if __name__ == '__main__':
    main()
