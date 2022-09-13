from math import inf
class Solution:
    def __helper (self, row, col, dest_row, dest_col, N):
        if ((row == dest_row) and (col == dest_col)):
            self.visited[row][col][0] = 0
            return 0
        self.visited[row][col][0] = inf
        self.visited[row][col][1] = True
        for row_offset, col_offset in self.dirs:
            next_row, next_col = row + row_offset, col + col_offset
            if ((0 <= next_row < N) and (0 <= next_col < N)):
                if (self.visited[next_row][next_col][0] == -1):
                    self.visited[row][col][0] = min(self.visited[row][col][0], self.__helper(next_row, next_col, dest_row, dest_col, N) + 1)
                elif (self.visited[next_row][next_col][1] == False):
                    self.visited[row][col][0] = min(self.visited[row][col][0], self.visited[next_row][next_col][0] + 1)
        self.visited[row][col][1] = False
        return self.visited[row][col][0]

    def minStepToReachTarget (self, KnightPos, TargetPos, N):
	    self.visited = [[[-1, False] for i in range(N)] for j in range(N)]
	    self.dirs = [(-2, 1), (-1, 2), (2, 1), (1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]
	    return self.__helper(KnightPos[0] - 1, KnightPos[1] - 1, TargetPos[0] - 1, TargetPos[1] - 1, N)
