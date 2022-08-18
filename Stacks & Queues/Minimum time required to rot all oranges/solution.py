from collections import deque
class Solution:
    def orangesRotting (self, grid):
	    q_for_rotten, dirs = deque(), [(0, 1), (0, -1), (-1, 0), (1, 0)]
	    fresh, time = 0, 0
	    for i in range(len(grid)):
	        for j in range(len(grid[0])):
	            if (grid[i][j] == 2): q_for_rotten.append((i, j, 0))
	            elif (grid[i][j] == 1): fresh += 1
        while (q_for_rotten):
            row, col, curr_time = q_for_rotten.popleft()
            time = max(time, curr_time)
            for row_offset, col_offset in dirs:
                next_row, next_col = row + row_offset, col + col_offset
                if ((0 <= next_row < len(grid)) and (0 <= next_col < len(grid[0])) and (grid[next_row][next_col] == 1)):
                    grid[next_row][next_col] = 2
                    q_for_rotten.append((next_row, next_col, curr_time + 1))
                    fresh -= 1
        return -1 if (fresh > 0) else time
