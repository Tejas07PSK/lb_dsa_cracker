from math import inf
from collections import deque
class Solution:
    def findCheapestPrice (self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        res = [inf for i in range(n)] ; res[src] = 0
        adj_lst = [[] for i in range(n)]
        for start, end, weight in flights: adj_lst[start].append([end, weight])
        stk = deque() ; stk.append((0, src, 0))
        while (stk):
            steps, curr_node, tot_wt = stk.popleft()
            for next_node, weight in adj_lst[curr_node]:
                if ((steps + 1) <= k):
                    if ((tot_wt + weight) < res[next_node]):
                        res[next_node] = tot_wt + weight
                        if (next_node != dst): stk.append(((steps + 1), next_node, (tot_wt + weight)))
                elif (((steps + 1) == k + 1) and (next_node == dst)):
                    res[next_node] = min(res[next_node], (tot_wt + weight))
        return (-1 if (res[dst] == inf) else res[dst])
