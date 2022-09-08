from heapq import _heapify_max
class Solution():
    def mergeHeaps (self, a, b, n, m):
        res = a + b
        _heapify_max(res)
        return res
