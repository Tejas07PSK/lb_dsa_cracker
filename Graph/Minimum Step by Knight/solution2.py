from math import inf
from collections import deque

class Solution:
    def minStepToReachTarget (self, KnightPos, TargetPos, N):
        if ((KnightPos[0] == TargetPos[0]) and (KnightPos[1] == TargetPos[1])): return 0
	    self.visited = [[inf for i in range(N)] for j in range(N)]
	    self.dirs = [(-2, 1), (-1, 2), (2, 1), (1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]
	    self.q = deque() ; self.q.append((KnightPos[0] - 1, KnightPos[1] - 1, 0))
	    self.visited[KnightPos[0] - 1][KnightPos[1] - 1] = 0
	    while (self.q):
	        row, col, dist_from_start = self.q.popleft()
	        for row_offset, col_offset in self.dirs:
                next_row, next_col = row + row_offset, col + col_offset
                if ((0 <= next_row < N) and (0 <= next_col < N) and (self.visited[next_row][next_col] == inf)):
                    self.visited[next_row][next_col] = dist_from_start + 1
                    if ((next_row == (TargetPos[0] - 1)) and (next_col == (TargetPos[1] - 1))): return self.visited[next_row][next_col]
                    self.q.append((next_row, next_col, self.visited[next_row][next_col]))
        return self.visited[TargetPos[0] - 1][TargetPos[1] - 1]
