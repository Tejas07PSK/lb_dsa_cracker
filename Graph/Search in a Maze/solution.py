from collections import deque

class Solution:
    def __findPathHelper (self, row, col, mat, n):
        if ((row == n - 1) and (col == n - 1)):
            self.res.append("".join(self.curr_path))
        mat[row][col] = 0
        for row_offset, col_offset, dir_str in self.dirs:
            next_row, next_col = row + row_offset, col + col_offset
            if ((0 <= next_row < n) and (0 <= next_col < n) and (mat[next_row][next_col] != 0)):
                self.curr_path.append(dir_str)
                self.__findPathHelper(next_row, next_col, mat, n)
                self.curr_path.pop()
        mat[row][col] = 1

    def findPath (self, m, n):
        if ((m[0][0] == 0) or (m[n - 1][n -1] == 0)): return []
        self.res, self.curr_path = [], deque()
        self.dirs = [(1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U')]
        self.__findPathHelper(0, 0, m, n)
        return self.res
