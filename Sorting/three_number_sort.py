"""
Time complexity: O(n)
Space complexity: O(1)
"""


def three_number_sort(array: 'list[int]', order: 'list[int]'):
    first_val = order[0]
    second_val = order[1]
    
    first_idx, second_idx, third_idx = 0, 0, len(array)-1
    while second_idx <= third_idx:
        current_value = array[second_idx]

        if current_value == first_val:
            array[first_idx], array[second_idx] = array[second_idx], array[first_idx]
            first_idx += 1
            second_idx += 1
        elif current_value == second_val:
            second_idx += 1
        else:
            array[second_idx], array[third_idx] = array[third_idx], array[second_idx]
            third_idx -= 1
        
    return array
    

def main() -> None:
    array = [1, 0, 0, -1, -1, 0, 1, 1]
    order = [0, 1, -1]
    ans = three_number_sort(array, order)

    print(f'The ans is: {ans}')


if __name__ == '__main__':
    main()
