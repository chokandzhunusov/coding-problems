"""
Time complexity: O(n + y) n => number of words; y => longest word, as you have to count at most to the longest word length.
Space complexity: O(c * x) c is number of all characters accross all words. x => how many times char appeared and will be populated to form final result array.
"""


def min_chars_for_words(array: 'list[str]') -> 'list[str]':
    result = []
    hash = {}
    for word in array:
        hash_for_word = {}

        # Count char frequencies per word.
        for char in word:
            if char not in hash_for_word:
                hash_for_word[char] = 0
            hash_for_word[char] += 1
        
        # Update the main hash if needed.
        # Case when char found in word doesn't exist in main hash.
        # Or the frequency is greater that it used to be in prev. words.
        for char in hash_for_word:
            if char in hash:
                hash[char] = max(hash[char], hash_for_word[char])
            else:
                hash[char] = hash_for_word[char]

    # Make a list out of chars and their amounts.
    for char in hash:
        for k in range(hash[char]):
            result.append(char)
    return result
    

def main() -> None:
    ans = min_chars_for_words(['this', 'that', 'did', 'deed', 'them!', 'a'])
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
