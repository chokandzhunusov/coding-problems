"""
Time complexity: O(log(n))
Space complexity: O(1)
"""


# def index_equals_value(array: 'list[int]') -> 'int':
#     for i, num in enumerate(array):
#         if i == num:
#             return i

#     return -1

    
def index_equals_value(array: 'list[int]') -> 'int':
    left_idx = 0
    right_idx = len(array) - 1
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if mid_idx > array[mid_idx]:
            left_idx = mid_idx + 1
        elif mid_idx == array[mid_idx] and mid_idx == 0:
            return mid_idx
        elif mid_idx == array[mid_idx] and array[mid_idx - 1] < mid_idx - 1:
            return mid_idx
        else:
            right_idx = mid_idx - 1
    return -1


def main() -> None:
    # array = [-5, -3, 0, 3, 4, 5, 9]
    array = [-40, -20, 2, 3, 4, 6, 8, 10]
    ans = index_equals_value(array)

    print(f'The ans is: {ans}')


if __name__ == '__main__':
    main()
