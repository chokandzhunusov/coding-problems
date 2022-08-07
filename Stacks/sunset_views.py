"""
Time complexity: O(n)
Space complexity: O(n)
"""


def sunset_views(buildings: 'list[int]', direction: 'str') -> 'list[int]':
    stack = []

    start_id = 0 if direction == 'EAST' else len(buildings) - 1
    step = 1 if direction == 'EAST' else -1
    
    while start_id >= 0 and start_id < len(buildings):
        current_child_height = buildings[start_id]
        
        while len(stack) > 0 and buildings[stack[-1]] <= current_child_height:
            stack.pop()
        
        stack.append(start_id)
        start_id += step

    if direction == 'WEST':
        return stack[::-1]

    return stack


def main() -> None:
    print(sunset_views([3, 5, 4, 4, 3, 1, 3, 2], 'EAST'))  # Right direction


if __name__ == '__main__':
    main()