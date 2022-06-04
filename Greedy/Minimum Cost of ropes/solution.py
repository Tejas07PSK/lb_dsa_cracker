from heapq import heapify, heappop, heappush
class Solution:
    def minCost (self, arr, n):
        heapify(arr) ; tot_cost = 0
        while (len(arr) > 1):
            new_rope_len = (heappop(arr) + heappop(arr))
            tot_cost += new_rope_len
            heappush(arr, new_rope_len)
        return tot_cost
