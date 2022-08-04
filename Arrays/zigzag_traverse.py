"""
Time complexity: O(n)
Space complexity: O(n)
"""


def zigzag_traverse(array: 'list[list[int], list[int]]'):
    height = len(array) - 1
    width = len(array[0]) - 1
    
    row, col = 0, 0

    down = True
    
    result = []
    
    while not out_of_bounce(row, col, height, width):
        result.append(array[row][col])
        if down:
            if col == 0 or row == height:
                # Position is at first column or last row
                down = False
                if row == height:
                    # Row is last row, move column
                    col += 1
                else:
                    # It's first column, move row. Keep going down
                    row += 1
            else:
                row += 1  # Go down
                col -= 1  # Go left 
        else:
            if row == 0 or col == width:
                # Top right perimeter
                down = True
                if col == width:
                    # Final col
                    row += 1
                else:
                    # First row but not top right corner
                    # Go right
                    col += 1
            else:
                # Not top right corner, inside of perimeter
                # Go dioganally upwards
                row -= 1 
                col += 1
    
    return result


def out_of_bounce(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width


def main() -> None:
    ans = zigzag_traverse([
        [1, 3, 4, 10],
        [2, 5, 9, 11],
        [6, 8, 12, 15],
        [7, 13, 14, 16]
    ])
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()