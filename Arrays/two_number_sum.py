"""
Time complexity: O(n)
Space complexity: O(n)
"""


def two_number_sum(array: "list[int]", target_sum: int) -> "list[int]":
    seen = []
    for n in array:
        if target_sum - n in seen:
            return [n, target_sum - n]
        seen.append(n)
    return []


def main() -> None:
    ans = two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10)
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
