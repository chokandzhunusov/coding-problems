"""
Time complexity: O(n + m)
Space complexity: O(k) num of unique chars
"""


def generate_document(characters: 'str', document: 'str') -> 'bool':
    characters_count = {}

    for char in characters:
        if char not in characters_count:
            characters_count[char] = 0
        characters_count[char] += 1
    
    for char in document:
        if char not in characters_count or characters_count[char] == 0:
            return False
        characters_count[char] -= 1
    return True
        

def main() -> None:
    ans = generate_document('Bste!hetsi  ', 'is the Best!')
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
