import numpy as np

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, 8, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_queens(board, col):
    if col >= 8:
        return True
    for i in range(8):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_queens(board, col + 1):
                return True
            board[i][col] = 0
    return False

def print_solution(board):
    print(np.flipud(board))

board = np.zeros((8, 8), dtype=int)
if solve_queens(board, 0):
    print_solution(board)
else:
    print("No solution exists")
