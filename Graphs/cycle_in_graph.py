"""
Time complexity: O(v + e) vertices + edges. In DFS look all vertces and edges.
Space complexity: O(v)
"""


def is_node_in_cycle(node: 'int', edges: 'list[list[int]]', visited: 'list[bool]', in_stack: 'list[bool]'):
    visited[node] = True
    in_stack[node] = True

    neighbours = edges[node]
    for neighbour in neighbours:
        if not visited[neighbour]:
            contains_cycle = is_node_in_cycle(neighbour, edges, visited, in_stack)
            if contains_cycle:
                return True
        elif in_stack[neighbour]:
            return True
    in_stack[node] = False
    return False


def cycle_in_graph(edges: 'list[list[int]]'):
    number_of_nodes = len(edges)
    visited = [False for _ in range(number_of_nodes)]
    in_stack = [False for _ in range(number_of_nodes)]

    for node in range(number_of_nodes):
        if visited[node]:
            continue
        contains_cycle = is_node_in_cycle(node, edges, visited, in_stack)
        if contains_cycle:
            return True
    
    return False


def main() -> None:
    edges = [
        [1, 3],
        [2, 3, 4],
        [0],
        [],
        [2, 5],
        []
    ]

    ans = cycle_in_graph(edges)
    print(f'The answer is: {ans}')

    
if __name__ == '__main__':
    main()
