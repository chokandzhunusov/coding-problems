"""
Time complexity: 
    - O(n * log(m)) n => for row, m => for elements in row.
    - Optimized: 
        O(n + m) n => for row and column.
Space complexity: O(1)
"""


def search_in_sorted_matrix(matrix: 'list[list[int]]', target: 'int'):
    for row_idx, row in enumerate(matrix):
        if target < row[0] or target > row[-1]:
            continue
        
        start_idx = 0
        end_idx = len(row) - 1
        while end_idx >= start_idx:
            mid_idx = (start_idx + end_idx) // 2
            potential_match = row[mid_idx]
            if target == potential_match:
                return [row_idx, mid_idx]
            elif target < potential_match:
                end_idx = mid_idx - 1
            else:
                start_idx = mid_idx + 1
    return [-1, -1]


def improved_search_in_sorted_matrix(matrix: 'list[list[int]]', target: 'int'):
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if target < matrix[row][col]:
            col -= 1
        elif target > matrix[row][col]:
            row += 1
        else:
            return [row, col]
    return [-1, -1]


def main() -> None:    
    matrix = [
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004]
    ]
    target = 103
    
    ans = improved_search_in_sorted_matrix(matrix, target)
    
    print(f'The ans is: {ans}')
    

if __name__ == '__main__':
    main()
