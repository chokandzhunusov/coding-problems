"""
Time complexity: O(n^2)
Space complexity: O(n) for slicing the string at the last step.
"""


def get_longest_palindrome_from(string, left_idx, right_idx):
    while left_idx >= 0 and right_idx < len(string):
        if string[left_idx] != string[right_idx]:
            break
        left_idx -= 1
        right_idx += 1
    return [left_idx + 1, right_idx]


def longest_palindromic_substring(string: 'str') -> 'str':
    current_longest = [0, 1]

    for i in range(len(string)):
        odd = get_longest_palindrome_from(string, i-1, i+1)
        even = get_longest_palindrome_from(string, i-1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        current_longest = max(current_longest, longest, key=lambda x: x[1] - x[0])
    return string[current_longest[0]:current_longest[1]]
        

def main() -> None:
    ans = longest_palindromic_substring('abaxyzaazyxf')
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
