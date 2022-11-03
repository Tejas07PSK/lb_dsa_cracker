from typing import List

class Solution:
    def vertexCover (self, n: int, m: int, edges: List[List[int]]) -> int:
        if (m == 0): return 1
        adj_lst = [[0 for j in range(n)] for i in range(n)]
        deg = [0 for i in range(n)]
        for start, end in edges:
            deg[start - 1] += 1 ; deg[end - 1] += 1
            adj_lst[start - 1][end - 1] = 1 ; adj_lst[end - 1][start - 1] = 1
        res = 0
        while (m > 0):
            mx_idx = 0
            for i in range(1, n):
                if (deg[i] > deg[mx_idx]): mx_idx = i
            m -= deg[mx_idx] ; deg[mx_idx] = 0 ; res += 1
            for i in range(n):
                if (adj_lst[mx_idx][i] == 1):
                    adj_lst[mx_idx][i] = 0 ; adj_lst[i][mx_idx] = 0
                    deg[i] -= 1
        return res
