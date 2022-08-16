"""
Time complexity: O(w*h) width and height of matrix
Space complexity: O(w*h) for auxilary matrix and stack.
"""


def get_adjacents(row, col, matrix, visited):
    adjacents = []
    if row > 0 and not visited[row-1][col]:
        adjacents.append([row-1, col])
    if row < len(matrix) - 1 and not visited[row+1][col]:
        adjacents.append([row+1, col])
    if col > 0 and not visited[row][col-1]:
        adjacents.append([row, col-1])
    if col < len(matrix[0])-1 and not visited[row][col+1]:
        adjacents.append([row, col+1])
    return adjacents


def node_is_not_island(row, col, matrix):
    height = len(matrix) - 1
    width = len(matrix[0]) - 1
    if row in [0, height] or col in [0, width]:
        return True
    return False


def breadth_first_search(row, col, matrix, visited):
    stack = [[row, col]]
    at_least_one_is_on_border = False
    potential_islands = []
    while len(stack) > 0:
        current_node = stack.pop()
        row, col = current_node
        if visited[row][col]:
            continue
        
        visited[row][col] = True

        if matrix[row][col] == 1:
            if node_is_not_island(row, col, matrix):
                at_least_one_is_on_border = True
            else:
                potential_islands.append([row, col])
            adjacents = get_adjacents(row, col, matrix, visited)
            [stack.append(adjacent) for adjacent in adjacents]
    if not at_least_one_is_on_border:
        for island in potential_islands:
            matrix[island[0]][island[1]] = 0


def remove_islands(matrix: 'list[list[int]]'):
    visited = [[False for col in row] for row in matrix]
    col = row = 0
    
    for row in range(len(visited)):
        for col in range(len(visited[row])):
            if visited[row][col]:
                continue
            breadth_first_search(row, col, matrix, visited)
    
    return matrix


def main() -> None:
    matrix = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1]
    ]

    modified_matrix = remove_islands(matrix)

    for row in range(len(modified_matrix)):
        for col in range(len(modified_matrix[row])):
            print(modified_matrix[row][col], end=' ')
        print(end='\n')
    

if __name__ == '__main__':
    main()
