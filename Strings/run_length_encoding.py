"""
Time complexity: O(n)
Space complexity: O(n)
"""


def run_length_encoding(string: 'str') -> 'str':
    result = []
    current_run_length = 1

    for i in range(1, len(string)):
        current_char = string[i]
        prev_char = string[i-1]

        if current_char != prev_char or current_run_length == 9:
            result.append(str(current_run_length))
            result.append(prev_char)
            current_run_length = 0
        
        current_run_length += 1
    
    result.append(str(current_run_length))
    result.append(string[-1])
    return ''.join(result)
    
        
def main() -> None:
    ans = run_length_encoding('AAAAAAAAAAAAABBCCCCDD')
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
