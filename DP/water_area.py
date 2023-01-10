"""
Time complexity: O(n)
Space complexity: O(1)
"""


def water_area(heights):
    if len(heights) == 0:
        return 0

    left_idx = 0
    right_idx = len(heights) - 1
    left_max = heights[left_idx]
    right_max = heights[right_idx]
    surface_area = 0

    while left_idx < right_idx:
        if heights[left_idx] < heights[right_idx]:
            left_idx += 1
            left_max = max(left_max, heights[left_idx])
            surface_area += left_max - heights[left_idx]
        else:
            right_idx -= 1
            right_max = max(right_max, heights[right_idx])
            surface_area += right_max - heights[right_idx]

    return surface_area

def main() -> None:
    heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
    print(water_area(heights))
    return


if __name__ == '__main__':
    main()