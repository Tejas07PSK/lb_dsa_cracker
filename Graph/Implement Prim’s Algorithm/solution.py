from heapq import heapify, heappush, heappop
class Solution:
    def spanningTree (self, v, adj_lst):
        visited, count, sum_so_far = set(), 1, 0
        min_heap = [(wt, 0, nxt_vrt) for nxt_vrt, wt in adj_lst[0]]
        heapify(min_heap) ; visited.add(0)
        while (count < v):
            wt, prev_vrt, curr_vrt = heappop(min_heap)
            if (curr_vrt not in visited):
                sum_so_far += wt ; count += 1 ; visited.add(curr_vrt)
                for nxt_vrt, wt in adj_lst[curr_vrt]:
                    if (nxt_vrt not in visited): heappush(min_heap, (wt, curr_vrt, nxt_vrt))
        return sum_so_far
