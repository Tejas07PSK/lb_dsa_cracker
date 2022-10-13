from collections import deque
from math import inf

class Solution:
    def maximumDistance(self, n, m, src, edges):
        in_deg_arr, adj_lst = [0 for i in range(n)], [[] for i in range(n)]
        q, res = deque(), [-inf for i in range(n)] ; res[src] = 0
        for start, end, weight in edges:
            in_deg_arr[end] += 1
            adj_lst[start].append([end, weight])
        for i in range(n):
            if (in_deg_arr[i] == 0): q.append(i)
        while (q):
            idx = q.popleft()
            for next_idx, wt in adj_lst[idx]:
                in_deg_arr[next_idx] -= 1
                res[next_idx] = max(res[next_idx], res[idx] + wt)
                if (in_deg_arr[next_idx] == 0): q.append(next_idx)
        for i in range(n):
            if (res[i] == -inf): res[i] = "INF"
        return res
