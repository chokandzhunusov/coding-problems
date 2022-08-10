"""
Time complexity: O(n)
Space complexity: O(1) given only alphabet chars, so hash will not exceed 26 characters.
"""


def first_non_repeating_char(string: 'str') -> 'int':
    hash_of_chars = {}

    for char in string:
        if char not in hash_of_chars:
            hash_of_chars[char] = 0
        hash_of_chars[char] += 1
    
    for i, char in enumerate(string):
        if hash_of_chars[char] == 1:
            return i
    return -1
        

def main() -> None:
    ans = first_non_repeating_char('abcdcaf')
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
