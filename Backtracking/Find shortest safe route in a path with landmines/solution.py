from collections import deque
from math import inf

class Solution:
    row_col_are_valid = lambda row, row_len, col, col_len: ((0 <= row < row_len) and (0 <= col <= col_len))
    dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def __bfs (self, row, col, n, m, path_matrix):
        if (path_matrix[row][col] == 0): return
        q, visited = deque(), set()
        q.append((row, col, 0))
        while (q):
            curr_row, curr_col, dist_so_far = q.popleft()
            if (curr_col == m - 1):
                self.res = min(self.res, dist_so_far) ; continue
            visited.add((curr_row, curr_col))
            is_safe = True
            for dir_row, dir_col in Solution.dirs:
                adj_row, adj_col = curr_row + dir_row, curr_col + dir_col
                if (Solution.row_col_are_valid(adj_row, n, adj_col, m) and (path_matrix[adj_row][adj_col] == 0)):
                    is_safe = False ; break
            if (is_safe):
                for dir_row, dir_col in Solution.dirs:
                    adj_row, adj_col = curr_row + dir_row, curr_col + dir_col
                    if (Solution.row_col_are_valid(adj_row, n, adj_col, m) and ((adj_row, adj_col) not in visited)):
                        q.append((adj_row, adj_col, dist_so_far + 1))

    def shortest_path_landmine (self, n, m, path_matrix):
        self.res = inf
        for i in range(n): self.__bfs(i, 0, n, m, path_matrix)
        return self.res
