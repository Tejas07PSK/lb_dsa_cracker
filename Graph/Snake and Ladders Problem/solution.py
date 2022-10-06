from collections import deque
class Solution:
    def snakesAndLadders (self, board: List[List[int]]) -> int:
        snakes_n_ladders, visited, n, steps = {}, set(), len(board) ** 2, 0
        count, col_start, col_end, col_offset = 0, 0, len(board) - 1, 1
        for row in range(len(board) - 1, -1, -1):
            col = col_start
            while ((col <= col_end) if (col_offset > 0) else (col >= col_end)):
                if (board[row][col] != -1): snakes_n_ladders[count] = (board[row][col] - 1)
                count += 1 ; col += col_offset
            col_start, col_end, col_offset = col_end, col_start, -col_offset
        stk = deque([0]) ; visited.add(0)
        while (stk):
            curr_stk_sz = len(stk)
            for i in range(curr_stk_sz):
                curr_pos = stk.popleft()
                for next_pos in range(curr_pos + 1, curr_pos + 7):
                    if (next_pos < n):
                        if (next_pos in snakes_n_ladders): next_pos = snakes_n_ladders[next_pos]
                        if (next_pos not in visited):
                            if (next_pos == (n - 1)): return (steps + 1)
                            visited.add(next_pos)
                            stk.append(next_pos)
            steps += 1
        return -1
