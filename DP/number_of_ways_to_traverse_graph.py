"""
Time complexity: O(n * m) for n: width, m: height
Space complexity: O(n * m)
"""

def number_of_ways_to_traverse_graph(width, height):
    number_of_ways = [[0 for _ in range(width+ 1 )] for _ in range(height + 1)]
    for width_idx in range(1, width + 1):
        for height_idx in range(1, height + 1):
            if width_idx == 1 or height_idx == 1:
                number_of_ways[height_idx][width_idx] = 1
            else:
                ways_left = number_of_ways[height_idx][width_idx - 1]
                ways_up = number_of_ways[height_idx -1][width_idx]
                number_of_ways[height_idx][width_idx] = ways_left + ways_up
    return number_of_ways[height][width]

def main() -> None:
    print(number_of_ways_to_traverse_graph(4, 3))
    return


if __name__ == '__main__':
    main()
