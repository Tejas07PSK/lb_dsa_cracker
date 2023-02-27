from heapq import heappush, heappop
class Solution:
    def findKthLargest (self, nums: List[int], k: int) -> int:
        mn_hp = []
        for num in nums:
            heappush(mn_hp, num)
            if (len(mn_hp) > k): heappop(mn_hp)
        return mn_hp[0]
