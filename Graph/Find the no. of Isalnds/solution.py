from collections import deque
class Solution:
    def numIslands (self, grid):
        n, m = len(grid), len(grid[0])
        visited = [[False if (grid[i][j] == 1) else True for j in range(m)] for i in range(n)]
        q, dirs = deque(), [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        island_count = 0
        for i in range(n):
            for j in range(m):
                if (not visited[i][j]):
                    visited[i][j] = True
                    island_count += 1
                    q.append((i, j))
                    while (q):
                        curr_row, curr_col = q.popleft()
                        for row_offset, col_offset in dirs:
                            next_row, next_col = curr_row + row_offset, curr_col + col_offset
                            if ((0 <= next_row < n) and (0 <= next_col < m) and (not visited[next_row][next_col])):
                                visited[next_row][next_col] = True
                                q.append((next_row, next_col))
        return island_count
