"""
Time complexity: O(n^2) even we are cutting the end of array. We still loop bunch of times over it.
Space complexity: O(1)
"""

    
def iterative_bubble_sort(array: 'list[int]') -> 'list[int]':
    sorted = False
    counter = 0
    while not sorted:
        sorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                sorted = False
        counter += 1    
    
    return array


def recursive_bubble_sort(array: 'list[int]') -> 'list[int]':
    swap_occured = False
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            array[i], array[i-1] = array[i-1], array[i]
            swap_occured = True
    if swap_occured:
        recursive_bubble_sort(array)
    
    return array


def main() -> None:
    array = [8, 5, 2, 9, 5, 6, 3]
    ans = iterative_bubble_sort(array)

    print(f'The ans is: {ans}')


if __name__ == '__main__':
    main()
