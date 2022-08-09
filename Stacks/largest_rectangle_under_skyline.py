"""
Time complexity: O(n)
Space complexity: O(n)
"""


def largest_rectangle_under_skyline(buildings: 'list[int]') -> 'int':
    stack = []
    max_area = 0
    for i, building in enumerate(buildings + [0]):
        while len(stack) != 0 and buildings[stack[-1]] >= building:
            building_height = buildings[stack.pop()]
            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1] - 1
            max_area = max(width*building_height, max_area)
       
        stack.append(i)
    return max_area


def main() -> None:
    ans = largest_rectangle_under_skyline([1, 3, 3, 2, 4, 1, 5, 3, 2])
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
