from heapq import heapify, heappush, heappop
class Solution:
    def minCost (self, arr, n):
        if (len(arr) == 0): return 0
        if (len(arr) == 1): return 0
        heapify(arr) ; cost = 0
        while (len(arr) > 1):
            tmp_sum = heappop(arr) + heappop(arr)
            cost += tmp_sum
            heappush(arr, tmp_sum)
        return cost
