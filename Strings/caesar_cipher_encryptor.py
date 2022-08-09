"""
Time complexity: O(n)
Space complexity: O(n)
"""


def caeser_cipher_encryptor(word: 'str', k: 'int') -> 'str':
    result = []
    k = k % 26  # Case when k > 26 is given 
    for letter in word:
        new_letter = ord(letter) + k
        if new_letter > 122:
            new_letter -= 26
        result.append(chr(new_letter))
    
    return ''.join(result)
        

def main() -> None:
    ans = caeser_cipher_encryptor('xyz', 2)
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
