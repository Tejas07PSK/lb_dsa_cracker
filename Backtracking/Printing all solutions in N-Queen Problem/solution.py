from collections import deque
class Solution:
    def __isSafe (self, row, col, n):
        i, j = row - 1, col - 1
        while ((i >= 0) and (j >= 0)):
            if (self.chess_board[i][j] == True): return False
            i, j = i - 1, j - 1
        i, j = row - 1, col
        while (i >= 0):
            if (self.chess_board[i][j] == True): return False
            i = i - 1
        i, j = row - 1, col + 1
        while ((i >= 0) and (j < n)):
            if (self.chess_board[i][j] == True): return False
            i, j = i - 1, j + 1
        return True

    def __nQueenHelper (self, row, n):
        if (row == n):
            self.ans.append(list(self.temp_ans))
            return
        for col in range(n):
            if (self.__isSafe(row, col, n)):
                self.chess_board[row][col] = True ; self.temp_ans.append(col + 1)
                self.__nQueenHelper(row + 1, n)
                self.chess_board[row][col] = False ; self.temp_ans.pop()

    def nQueen (self, n):
        self.ans, self.temp_ans = [], deque()
        self.chess_board = [[False for i in range(n)] for j in range(n)]
        self.__nQueenHelper(0, n)
        return self.ans
