"""
Time complexity: O(n)
Space complexity: O(n)
"""


def next_greater_element(array: 'list[int]') -> 'list[int]':
    result = [-1 for _ in array]
    stack = []

    for i in range(2 * len(array)):  # Bcs last should pointing to first from question
        # To prevent out of index array, when looping second time
        # 7 % 7 = 0 => we will start from beggining of an array
        circular_index = i % len(array)  
        while len(stack) > 0 and array[stack[-1]] < array[circular_index]:
            top = stack.pop()
            result[top] = array[circular_index]
        stack.append(circular_index)
    return result


def main() -> None: 
    print(next_greater_element([2, 5, -2, -4, 6, 7, 2]))
   

if __name__ == '__main__':
    main()