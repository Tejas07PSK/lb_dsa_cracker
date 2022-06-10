from collections import deque
class Solution:
    def __nQueenHelper (self, row, n):
        if (row == n):
            self.ans.append(self.temp_ans.copy())
            return
        for col in range(n):
            if (isSafe(row, col)):
                self.chess_board[row][col] = True
                self.temp_ans[row] = col + 1
                self.__nQueenHelper(row + 1, n)
                self.chess_board[row][col] = False
                self.temp_ans[row] = col + 1
    def nQueen (self, n):
        self.ans, self.temp_ans = [], deque()
        self.chess_board = [[False for i in range(n)] for j in range(n)]
        self.__nQueenHelper(0, n)