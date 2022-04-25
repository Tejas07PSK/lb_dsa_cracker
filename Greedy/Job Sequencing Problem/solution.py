from heapq import heappush, heappop
class Solution:
    def JobScheduling (self, jobs, n):
        min_heap = [] ; jobs.sort(key=lambda x: x.deadline)
        for i in range(n):
            heappush(min_heap, jobs[i].profit)
            while (len(min_heap) > jobs[i].deadline): heappop(min_heap)
        ans = [len(min_heap), 0]
        for p in min_heap: ans[1] += p
        return ans
