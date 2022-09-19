from typing import List
from collections import deque

class Solution:
    def minimumTime (self, n : int, m : int, edges : List[List[int]]) -> int:
        times, in_deg_arr, q = [0 for i in range(n)], [0 for i in range(n)], deque()
        adj_lst = [[] for i in range(n)]
        for start, end in edges:
            start -= 1 ; end -= 1
            adj_lst[start].append(end)
            in_deg_arr[end] += 1
        for i in range(n):
            if (in_deg_arr[i] == 0): q.append(i)
        time = 0
        while (q):
            time += 1 ; curr_sz = len(q)
            for i in range(curr_sz):
                curr_vert = q.popleft() ; times[curr_vert] = str(time)
                for next_vert in adj_lst[curr_vert]:
                    in_deg_arr[next_vert] -= 1
                    if (in_deg_arr[next_vert] == 0): q.append(next_vert)
        return " ".join(times)
