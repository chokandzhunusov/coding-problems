"""
Time complexity: O(n)
Space complexity: O(n)
"""


def is_important_token(token):
    return len(token) > 0 and token != '.'


def shorten_path(path: 'str') -> 'str':
    root_path = path[0] == '/'
    # Remove all empty strings and current directories
    # '', '.'
    tokens = filter(is_important_token, path.split('/'))
    stack = []

    if root_path:
        stack.append('')

    for token in tokens:
        if token == '..':
            if len(stack) == 0 or stack[-1] == '..':
                stack.append(token)
            elif stack[-1] != '':  # if not root dir
                stack.pop()
        else:
            # Token is path name
            stack.append(token)
    
    if len(stack) == 1 and stack[0] == '':
        # Only root directory
        return '/'
            
    return '/'.join(stack)


def main() -> None: 
    print(shorten_path('../../foo/../test/../test/../foo//bar/./baz'))
   

if __name__ == '__main__':
    main()