from typing import List
from heapq import heappush, heappop
from math import inf

class Solution:
    def __dijkstra (self, v, adj_lst, s):
        tmp_hm = [inf for i in range(v)] ; tmp_hm[s] = 0
        min_heap = [(0, s)]
        while (min_heap):
            dist_so_far, curr_node = heappop(min_heap)
            for next_node, weight in adj_lst[curr_node]:
                if ((dist_so_far + weight) < tmp_hm[next_node]):
                    tmp_hm[next_node] = dist_so_far + weight
                    heappush(min_heap, (tmp_hm[next_node], next_node))
        return tmp_hm

    def minimumEdgeReversal (self, edges: List[List[int]], n: int, m: int, src: int, dst: int) -> int:
        adj_lst = [[] for i in range(n)]
        for start, end in edges:
            adj_lst[start - 1].append([end - 1, 0])
            adj_lst[end - 1].append([start - 1, 1])
        return self.__dijkstra(n, adj_lst, src - 1)[dst - 1]
