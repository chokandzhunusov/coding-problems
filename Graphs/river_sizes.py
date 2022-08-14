"""
Time complexity: O(n*m) for width and height of matrix.
Space complexity: O(n*m) we might end up storing all elements.
"""


def traverse_node(row, col, matrix, visited, sizes):
    current_river_size = 0
    nodes_to_explore = [[row, col]]
    while len(nodes_to_explore):
        current_node = nodes_to_explore.pop()
        row = current_node[0]
        col = current_node[1]
        if visited[row][col]:
            continue
        visited[row][col] = True
        if matrix[row][col] == 0:
            continue
        current_river_size += 1
        unvisited_neighbors = get_unvisited_neighbors(row, col, matrix, visited)
        for neighbor in unvisited_neighbors:
            nodes_to_explore.append(neighbor)
    if current_river_size > 0:
        sizes.append(current_river_size)


def get_unvisited_neighbors(row, col, matrix, visited):
    unvisited_neighbors = []
    if row > 0 and not visited[row-1][col]:
        unvisited_neighbors.append([row-1, col])

    if row < len(matrix) - 1 and not visited[row+1][col]:
        unvisited_neighbors.append([row+1, col])

    if col > 0 and not visited[row][col - 1]:
        unvisited_neighbors.append([row, col - 1])

    if col < len(matrix[0]) - 1 and not visited[row][col + 1]:
        unvisited_neighbors.append([row, col + 1])
    
    return unvisited_neighbors
    

def river_sizes(matrix):
    sizes = []
    visited = [[False for value in row] for row in matrix]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if visited[row][col]:
                continue
            traverse_node(row, col, matrix, visited, sizes)
    return sizes


def main() -> None:
    matrix = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0],
    ]

    ans = river_sizes(matrix)
    
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
