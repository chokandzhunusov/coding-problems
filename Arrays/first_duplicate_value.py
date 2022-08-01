"""
Time complexity: O(n)
Space complexity: O(n)

Optimal 1:
    Time complexity: O(n)
    Space complexity: O(1)

"""
    

def first_duplicate_value(array: 'list[int]') -> 'int':
    seen = set()
    for num in array:
        if num in seen:
            return num
        seen.add(num)
    return -1


def first_duplicate_value_optimal_1(array: 'list[int]') -> 'int':
    for i, num in enumerate(array):
        if (array[abs(num) - 1] < 0):
            return abs(num)
        array[abs(num) - 1] *= -1
    return -1


def main() -> None:
    # ans = first_duplicate_value([2, 1, 5, 2, 3, 3, 4])
    ans = first_duplicate_value_optimal_1([2, 1, 5, 3, 3, 2, 4])
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
