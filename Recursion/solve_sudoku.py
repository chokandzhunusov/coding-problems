"""
Time complexity: O(1) bcs we will alwasy have the 9X9 board.
Space complexity: O(1)
"""


def solveSudoku(board):
    solve_partial_sudoku(0, 0, board)
    return board


def solve_partial_sudoku(row, col, board):
    current_row = row
    current_col = col

    if current_col == len(board[current_row]):
        # Go to next row
        current_row += 1
        current_col = 0
        if current_row == len(board):
            return True  # Board is completed

    if board[current_row][current_col] == 0:
        return try_digits_at_position(current_row, current_col, board)
    return solve_partial_sudoku(current_row, current_col + 1, board)


def try_digits_at_position(row, col, board):
    for digit in range(1, 10):
        if is_valid_at_position(digit, row, col, board):
            board[row][col] = digit
            if solve_partial_sudoku(row, col + 1, board):
                return True
    board[row][col] = 0
    return False


def is_valid_at_position(val, row, col, board):
    row_is_valid = val not in board[row]
    col_is_valid = val not in map(lambda r: r[col], board)

    if not row_is_valid or not col_is_valid:
        return False

    sub_grid_row_start = (row // 3) * 3
    sub_grid_col_start = (col // 3) * 3
    for row_idx in range(3):
        for col_idx in range(3):
            row_to_check = sub_grid_row_start + row_idx
            col_to_check = sub_grid_col_start + col_idx
            existing_value = board[row_to_check][col_to_check]

            if existing_value == val:
                return False
    return True
            
    
def main() -> None:
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    expected = [
        [7, 8, 5, 4, 3, 9, 1, 2, 6],
        [6, 1, 2, 8, 7, 5, 3, 4, 9],
        [4, 9, 3, 6, 2, 1, 5, 7, 8],
        [8, 5, 7, 9, 4, 3, 2, 6, 1],
        [2, 6, 1, 7, 5, 8, 9, 3, 4],
        [9, 3, 4, 1, 6, 2, 7, 8, 5],
        [5, 7, 8, 3, 9, 4, 6, 1, 2],
        [1, 2, 6, 5, 8, 7, 4, 9, 3],
        [3, 4, 9, 2, 1, 6, 8, 5, 7],
        ]
    assert solveSudoku(board) == expected
    

if __name__ == '__main__':
    main()
