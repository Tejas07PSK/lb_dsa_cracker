from heapq import heapify, heappop, heappush
from collections import defaultdict

class Solution:
    def minValue (self, s, k):
        hm = defaultdict(lambda : 0)
        for ch in s: hm[ch] -= 1
        hp = list(hm.values()) ; heapify(hp)
        while (k > 0):
            num = heappop(hp) ; num += 1
            if (num < 0): heappush(hp, num)
            k -= 1
        ans = 0
        for item in hp: ans += (item ** 2)
        return ans
