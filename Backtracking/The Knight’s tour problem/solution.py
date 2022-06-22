dirs = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]

def displayBoard (chess_board):
    for item in chess_board: print(item)

def knightTourHelper (chess_board, row, col, n, m, move_number):
    if ((row < 0) or (col < 0) or (row >= n) or (col >= m) or (chess_board[row][col] > 0)): return False
    elif (move_number == (n * m)):
        chess_board[row][col] = move_number ; return True
    chess_board[row][col] = move_number
    for row_offset, col_offset in dirs:
        if (knightTourHelper(chess_board, row + row_offset, col + col_offset, n, m, move_number + 1)): return True
    chess_board[row][col] = 0
    return False

def knightTour (n, m):
    chess_board = [[0 for j in range(m)] for i in range(n)]
    if (knightTourHelper(chess_board, 0, 0, n, m, 1)):
        print("Possible") ; displayBoard(chess_board)
    else: print("Impossible")
