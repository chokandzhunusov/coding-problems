"""
Time complexity: O(n)
Space complexity: O(1)
"""
    

def move_element_to_end(array: 'list[int]', num_to_move: 'int') -> 'list[int]':
    i = 0
    j = len(array) - 1

    while i < j:
        if array[i] == num_to_move and array[j] != num_to_move:
            swap = array[j]
            array[j] = array[i]
            array[i] = swap
        elif array[i] != num_to_move:
            i += 1
        elif array[j] == num_to_move:
            j -= 1
   
    return array


def move_element_to_end_2(array: 'list[int]', num_to_move: 'int') -> 'list[int]':
    end_index = len(array) - 1
    while end_index >= 0:
        if num_to_move == array[end_index]:
            array.pop(end_index)
            array.append(num_to_move)
        end_index -= 1
    return array


def main() -> None:
    ans = move_element_to_end([2, 1, 2, 2, 2, 3, 4, 2], 2)
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
