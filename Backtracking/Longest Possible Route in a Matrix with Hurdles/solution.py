class Solution:
    def __longestPathHelper (self, matrix, path, n, m, x, y, xd, yd):
        self.visited.add((x, y))
        for x_offset, y_offset in self.dirs:
            temp_x, temp_y = x + x_offset, y + y_offset
            if ((0 <= temp_x < n) and (0 <= temp_y < m) and ((temp_x, temp_y) not in self.visited) and (matrix[temp_x][temp_y] != 0)):
                if ((temp_x == xd) and (temp_y == yd)):
                    self.ans = max(self.ans, path + 1)
                else:
                    self.__longestPathHelper(matrix, path + 1, n, m, temp_x, temp_y, xd, yd)
        self.visited.discard((x, y))

    def longestPath (self, matrix, n, m, xs, ys, xd, yd):
        if (matrix[xs][ys] == 0): return -1
        self.visited, self.ans = set(), -1
        self.dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.__longestPathHelper(matrix, 0, n, m, xs, ys, xd, yd)
        return self.ans
