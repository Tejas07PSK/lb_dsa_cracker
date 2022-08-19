from collections import deque
from math import inf
class Solution:
	def nearest (self, grid):
	    q = deque()
	    res = [[inf for j in range(len(grid[0]))] for i in range(len(grid))]
	    dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
	    for i in range(len(grid)):
	        for j in range(len(grid[0])):
	            if (grid[i][j] == 1):
	                res[i][j] = 0
	                q.append((i, j))
	    while (q):
	        row, col = q.popleft()
	        for row_offset, col_offset in dirs:
	            next_row, next_col = row + row_offset, col + col_offset
	            if ((0 <= next_row < len(grid)) and (0 <= next_col < len(grid[0])) and (grid[next_row][next_col] == 0)):
	                res[next_row][next_col] = min(res[next_row][next_col], (res[row][col] + 1))
	                grid[next_row][next_col] = 1
	                q.append((next_row, next_col))
	    return res
