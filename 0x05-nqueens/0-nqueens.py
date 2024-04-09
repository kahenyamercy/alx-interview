#!/usr/bin/python3
"""
N Queens Problem Solver

Usage: nqueens.py N
  - N: An integer rep size of the chessboard and the number of queens.

Prints every possible solution to the problem, one solution per line.
Each solution is represented as a list of queen positions (row, column).
"""
import sys


def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at the given position (row, col)."""
    for i in range(row):
        if board[i][col] == 1 or \
            (col-row+i >= 0 and board[i][col-row+i] == 1) or \
                (col+row-i < N and board[i][col+row-i] == 1):
            return False
    return True


def solve_n_queens_util(board, row, N, result):
    """Recursively solve the N Queens problem."""
    if row == N:
        result.append([[i, j] for i in
                       range(N) for j in range(N) if board[i][j] == 1])
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, N, result)
            board[row][col] = 0


def solve_n_queens(N):
    """Solve the N Queens problem and print the solutions."""
    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    result = []
    solve_n_queens_util(board, 0, N, result)
    for solution in result:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    solve_n_queens(sys.argv[1])
