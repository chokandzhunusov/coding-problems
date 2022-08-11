"""
Time complexity: O(n)
Space complexity: O(n)
"""


def reverse_array(array: 'list[str]') -> 'list[str]':
    start, end = 0, len(array) - 1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    

def reverse_words_in_string(string: 'str') -> 'str':
    result = []
    start_of_word = 0

    for i in range(len(string)):
        if string[i] == ' ':
            result.append(string[start_of_word:i])
            start_of_word = i
        elif string[start_of_word] == ' ':
            result.append(' ')
            start_of_word = i
        
    result.append(string[start_of_word:])
    
    reverse_array(result)
    
    return ''.join(result)
    

def main() -> None:
    ans = reverse_words_in_string('tim is great')
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
