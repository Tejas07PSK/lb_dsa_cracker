from heapq import _heapify_max, _heappop_max

class Solution:
    def kLargest (self, arr, n, k):
        res = [] ; _heapify_max(arr)
        while (k > 0):
            res.append(_heappop_max(arr)) ; k -= 1
        return res
