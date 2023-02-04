class Solution:
    def jobScheduling (self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]
        jobs.sort(key=(lambda x : x[0]))
        dp = [None for i in range(len(jobs))] ; dp[-1] = jobs[-1][2]
        for i in range(len(jobs) - 2, -1, -1):
            dp[i] = jobs[i][2]
            low, high = i + 1, len(jobs) - 1
            while (low <= high):
                mid = low + ((high - low) // 2)
                if (jobs[mid][0] >= jobs[i][1]):
                    dp[i] = max(dp[i], (jobs[i][2] + dp[mid]))
                    high = mid - 1
                else: low = mid + 1
            dp[i] = max(dp[i], dp[i + 1])
        return dp[0]
