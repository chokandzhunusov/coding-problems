"""
Time complexity: O()
Space complexity: O()
"""


class MinMaxStack:
    def __init__(self):
        self.min_max_pairs = []
        self.stack = []

    def peek(self):
        return self.stack[-1]

    def pop(self):
        self.min_max_pairs.pop()
        return self.stack.pop()

    def push(self, number):
        new_min_max = {'min': number, 'max': number}
        if len(self.min_max_pairs):
            current_min_max_pair = self.min_max_pairs[-1]
            new_min_max['min'] = min(current_min_max_pair['min'], number)
            new_min_max['max'] = max(current_min_max_pair['max'], number)
        self.min_max_pairs.append(new_min_max)

        self.stack.append(number)

    def getMin(self):
        return self.min_max_pairs[-1]['min']

    def getMax(self):
        return self.min_max_pairs[-1]['max']


def main() -> None:
    stack = MinMaxStack()
    stack.push(5)
    print(stack.getMin())
    print(stack.getMax())
    print(stack.peek())
    print('='*10)
    stack.push(7)
    print(stack.getMin())
    print(stack.getMax())
    print(stack.peek())
    print('='*10)
    stack.push(2)
    print(stack.getMin())
    print(stack.getMax())
    print(stack.peek())

    print('='*10)
    print(stack.pop())
    print(stack.pop())
    print(stack.getMin())
    print(stack.getMax())
    print(stack.peek())


if __name__ == '__main__':
    main()