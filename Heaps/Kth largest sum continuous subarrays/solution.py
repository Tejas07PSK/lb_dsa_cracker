from typing import List
from heapq import heappop, heappush
class Solution:
    def kthLargest (self, N: int, K: int, Arr: List[int]) -> int:
        hp = []
        for i in range(len(Arr)):
            sof_sub_arr = 0 
            for j in range(i, len(Arr)):
                sof_sub_arr += Arr[j]
                if (len(hp) < K): heappush(hp, sof_sub_arr)
                elif (hp[0] < sof_sub_arr):
                    heappop(hp) ; heappush(hp, sof_sub_arr)
        return hp[0]
