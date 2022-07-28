"""
Time complexity: O(n)
Space complexity: O(1)
"""


def sorted_squared_array(array: "list[int]") -> "list[int]":
    return sorted([n*n for n in array])


def main() -> None:
    ans = sorted_squared_array([1, 2, 3, 5, 6, 8, 9])
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
