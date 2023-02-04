from heapq import heappush, heappop
class Solution:
    def jobScheduling (self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [[endTime[i], startTime[i], profit[i]] for i in range(len(startTime))]
        jobs.sort(key=(lambda x : x[1]))
        hp, ans, last_max_profit = [jobs[0]], jobs[0][2], 0
        for i in range(1, len(jobs)):
            ans = max(ans, jobs[i][2])
            while ((hp) and (jobs[i][1] >= hp[0][0])): last_max_profit = max(last_max_profit, heappop(hp)[2])
                
            jobs[i][2] = last_max_profit + jobs[i][2]
            ans = max(ans, jobs[i][2])
            heappush(hp, jobs[i])
        return ans
