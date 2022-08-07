"""
Time complexity: O()
Space complexity: O()
"""


def get_associated_opening_pair(char):
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    return pairs.get(char)


def balance_brackets(string):
    opening_brackets = set(['(', '{', '['])
    closing_brackets = set([')', '}', ']'])
    stack = []
    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not len(stack):
                return False
            elif stack[-1] == get_associated_opening_pair(char):
                stack.pop()
            else:
                return False
    return True if not stack else False


def main() -> None:
    print(balance_brackets('([])(){}(())()()'))
   

if __name__ == '__main__':
    main()