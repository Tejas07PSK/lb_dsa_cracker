from heapq import heappush, heappop
class Solution:
    def mergeKArrays (self, arr, k):
        hp, res = [], []
        for i in range(k): heappush(hp, (arr[i][0], i, 0))
        while (hp):
            element, row, col = heappop(hp)
            res.append(element)
            if ((col + 1) < len(arr[row])): heappush(hp, (arr[row][col + 1], row, col + 1))
        return res
