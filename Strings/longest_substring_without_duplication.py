"""
Time complexity: O(n)
Space complexity: O(min(n,a)) a => is max number of non duplicate charachters that we store.
"""


def longest_substring_without_duplication(string: 'str') -> 'str':
    seen = {}
    start_idx = 0
    longest = [0, 1]
    for current_idx, char in enumerate(string):
        if char in seen:
            start_idx = max(start_idx, seen[char]+1)
        
        if longest[1] - longest[0] < current_idx + 1 - start_idx:
            longest = [start_idx, current_idx + 1]
        
        seen[char] = current_idx
        
    return string[longest[0]:longest[1]]


def main() -> None:
    ans = longest_substring_without_duplication('abccdeaabbcddef')
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
