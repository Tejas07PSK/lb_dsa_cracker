from heapq import heapify, heappop

class Solution:
    def kthSmallest (self, arr, l, r, k):
        res = None ; heapify(arr)
        while (k > 0):
            res = heappop(arr) ; k -= 1
        return res
