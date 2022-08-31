from heapq import heapify, heappush, heappop
from math import inf
class Solution:
    def smallestRange(self, KSortedArray, n, k):
        ans = [inf, -inf]
        hp, rng_min, rng_max = [], inf, -inf
        for i in range(k):
            hp.append((KSortedArray[i][0], i, 0))
            rng_min = min(rng_min, KSortedArray[i][0])
            rng_max = max(rng_max, KSortedArray[i][0])
        ans[0], ans[1] = rng_min, rng_max
        heapify(hp)
        while (hp):
            element, row, col = heappop(hp)
            if ((rng_max - element + 1) < (ans[1] - ans[0] + 1)):
                rng_min = element
                ans[0] = rng_min
                ans[1] = rng_max
            if ((col + 1) < n):
                col += 1
                element = KSortedArray[row][col]
                heappush(hp, (element, row, col))
                rng_max = max(rng_max, element)
            else: break
        return ans
