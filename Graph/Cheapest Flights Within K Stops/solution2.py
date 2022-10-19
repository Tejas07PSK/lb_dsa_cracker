from math import inf
class Solution:
    def findCheapestPrice (self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        res = [inf for i in range(n)] ; res[src] = 0
        for i in range(k + 1):
            tmp = list(res)
            for start, end, weight in flights:
                tmp[end] = min(tmp[end], (res[start] + weight))
            res = tmp
        return (-1 if (res[dst] == inf) else res[dst])
