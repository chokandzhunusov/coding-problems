"""
Time complexity: O(n)
Space complexity: O(1)
"""


def shift_and_update(result: 'list[int]', num: 'int', idx: 'int'):
    for i in range(idx + 1):
        if i == idx:
            result[i] = num
        else:
            result[i] = result[i + 1]
    

def update_result(result: 'list[int]', num: 'int'):
    if not result[2] or num > result[2]:
        shift_and_update(result, num, 2)
    elif not result[1] or num > result[1]:
        shift_and_update(result, num, 1)
    elif not result[0] or num > result[0]:
        shift_and_update(result, num, 0)
    

def find_three_largest_numbers(array: 'list[int]'):
    result = [None for i in range(3)]
    for num in array:
        update_result(result, num)
    return result
    

def main() -> None:    
    array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
    ans = find_three_largest_numbers(array)
    
    print(f'The ans is: {ans}')
    

if __name__ == '__main__':
    main()
