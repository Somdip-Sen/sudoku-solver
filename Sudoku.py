# board = [
#     [7, 8, 0, 4, 0, 0, 1, 2, 0],
#     [6, 0, 0, 0, 7, 5, 0, 0, 9],
#     [0, 0, 0, 6, 0, 1, 0, 7, 8],
#     [0, 0, 7, 0, 4, 0, 2, 0, 0],
#     [0, 0, 1, 0, 5, 0, 9, 3, 0],
#     [9, 0, 4, 0, 6, 0, 0, 0, 5],
#     [0, 7, 0, 3, 0, 0, 0, 1, 2],
#     [1, 2, 0, 0, 0, 7, 4, 0, 0],
#     [0, 4, 9, 2, 0, 6, 0, 0, 7]
# ]
import time

def show_sudoku(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("----------------------\n")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end='')
            print(board[i][j], end=" ")
        print('\n')


def is_valid(i, j, num,board):
    row_valid = all(board[n][j] != num for n in range(9))
    if row_valid:
        valid = all(board[i][n] != num for n in range(9)) and all(
            board[x][y] != num for x in range(i // 3 * 3, i // 3 * 3 + 3) for y in range(j // 3 * 3, j // 3 * 3 + 3))
        return valid
    return False


def solvable(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return -1, -1


def solve(i, j, board):
    i, j = solvable(board)
    if i == -1:
        return True
    for num in range(1, 10):
        if is_valid(i, j, num,board):
            board[i][j] = num
            time.sleep(0.5)
            if solve(i, j, board):
                return True
            board[i][j] = 0
    return False


if __name__ == "__main__":
    board = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 0, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]]
    solve(0, 0, board)
    show_sudoku(board)
