"""
Time complexity: O(n)
Space complexity: O(1)
"""


def validate_subsequence(array: "list[int]", sequence: "list[int]") -> "bool":
    i = j = 0
    while i < len(array) and j < len(sequence):
        if array[i] == sequence[j]:
            j += 1
        i += 1
    return j == len(sequence)


def main() -> None:
    ans = validate_subsequence([1, 1, 1, 1, 1], [1, 1, 1])
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
