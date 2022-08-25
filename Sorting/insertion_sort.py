"""
Time complexity: O(n^2)
Space complexity: O(1)
"""

    
def insertion_sort(array: 'list[int]') -> 'list[int]':
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array


def main() -> None:
    array = [8, 5, 2, 9, 5, 6, 3]
    ans = insertion_sort(array)

    print(f'The ans is: {ans}')


if __name__ == '__main__':
    main()
