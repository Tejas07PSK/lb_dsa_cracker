from heapq import heappush, heappop

class Solution:
    def kthSmallest (self, arr, l, r, k):
        mx_hp = []
        for num in arr:
            heappush(mx_hp, -num)
            if (len(mx_hp) > k): heappop(mx_hp)
        return -mx_hp[0]
