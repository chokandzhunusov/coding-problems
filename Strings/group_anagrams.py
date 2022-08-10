"""
Time complexity: O(w*n*log^n ) w => anagrams given, n len of longest word 
Space complexity: O(wn)
"""


def group_anagrams(anagrams: 'list[str]') -> 'list[str]':
    hash = {}

    for word in anagrams:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in hash:
            hash[sorted_word] = []
        hash[sorted_word].append(word)
    return list(hash.values())
        

def main() -> None:
    ans = group_anagrams(['yo', 'act', 'flop', 'tac', 'foo', 'cat', 'oy', 'olfp'])
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
