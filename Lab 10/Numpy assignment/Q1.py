import random

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row-1, -1, -1), range(col+1, 8)):
        if board[i][j] == 'Q':
            return False
    return True

def solve_queens_randomized():
    board = [['.' for _ in range(8)] for _ in range(8)]
    cols = list(range(8))
    random.shuffle(cols)
    
    def backtrack(row):
        if row == 8:
            return True
        for col in cols:
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                if backtrack(row + 1):
                    return True
                board[row][col] = '.'
        return False
    
    if backtrack(0):
        print_board(board)
    else:
        print("No solution found")

solve_queens_randomized()
