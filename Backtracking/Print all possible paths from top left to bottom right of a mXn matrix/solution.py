from collections import deque
class Solution:
    def __allPathsFromTopLeftToBottomRightHelper (self, i, j, n, m):
        if ((i == n - 1) and (j == m - 1)):
            self.res.append("".join(self.tmp_path))
            return
        for i_offset, j_offset, direc in self.dirs:
            next_i, next_j = i + i_offset, j + j_offset
            if ((next_i < n) and (next_j < m)):
                self.tmp_path.append(direc)
                self.__allPathsFromTopLeftToBottomRightHelper(next_i, next_j, n, m)
                self.tmp_path.pop()

    def allPathsFromTopLeftToBottomRight (self, n, m):
        self.dirs, self.res, self.tmp_path = [(1, 0, 'D'), (0, 1, 'L')], [], deque()
        self.__allPathsFromTopLeftToBottomRightHelper(0, 0, n, m)
        return self.res
