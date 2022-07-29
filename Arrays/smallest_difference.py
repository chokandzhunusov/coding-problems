"""
Time complexity: O(nlon(n) + mlog(m)) for sorting arrays.
Space complexity: O(1)
"""


def smallest_difference(array_1: 'list[int]', array_2: 'list[int]') -> 'list[int]':
    array_1.sort()
    array_2.sort()
    
    smallest_diff = float('inf')
    smallest_pair = float('inf')
    current = float('inf')
    i = j = 0
    
    while i < len(array_1) and j < len(array_2):
        num_one = array_1[i]
        num_two = array_2[j]
        if num_one == num_two:
            return [num_one, num_two]
        elif num_one < num_two:
            current = num_two - num_one
            i += 1
        else:
            current = num_one - num_two
            j += 1
        
        if current < smallest_diff:
            smallest_diff = current
            smallest_pair = [num_one, num_two]
    return smallest_pair


def main() -> None:
    ans = smallest_difference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17])
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
