"""
Time complexity: O(w*h) width and height of matrix. Assuming that pop() takes constant time.
Space complexity: O(w*h)
"""


def get_neighbours(row: 'int', col: 'int', matrix: 'list[list[int]]'):
    neighbours = []
    if row > 0:
        neighbours.append([row-1, col])
    if row < len(matrix) - 1:
        neighbours.append([row+1, col])
    if col > 0:
        neighbours.append([row, col-1])
    if col < len(matrix[0]) - 1:
        neighbours.append([row, col+1])
    return neighbours


def get_positive_positions(matrix: 'list[list[int]]'):
    positive_positions = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            value = matrix[row][col]
            if value > 0:
                positive_positions.append([row, col])
    return positive_positions

    
def convert_negatives(matrix: 'list[list[int]]'):
    queue = get_positive_positions(matrix)
    passes = 0

    while len(queue) > 0:
        current_size = len(queue)
        while current_size > 0:
            current_row, current_col = queue.pop(0)
            neighbours = get_neighbours(current_row, current_col, matrix)
            for neighbour in neighbours:
                row, col = neighbour
                value = matrix[row][col]
                if value < 0:
                    matrix[row][col] *= -1
                    queue.append([row, col])
            current_size -= 1
        passes += 1
    return passes


def contains_negative(matrix: 'list[list[int]]'):
    for row in matrix:
        for value in row:
            if value < 0:
                return True
    return False


def minimum_passes_of_matrix(matrix: 'list[list[int]]'):
    passes = convert_negatives(matrix)
    return passes - 1 if not contains_negative(matrix) else -1


def main() -> None:
    matrix = [
        [0, -2, -1],
        [-5, 2, 0],
        [-6, -2, 0],
    ]

    ans = minimum_passes_of_matrix(matrix)
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print(matrix[row][col], end=' ')
        print(end='\n')
    print(f'The answer is: {ans}')

    
if __name__ == '__main__':
    main()
