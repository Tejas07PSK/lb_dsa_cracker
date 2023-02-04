class Solution:
    def __job_scheduling_helper (self, i, n):
        if (i == n): return self.jobs[i][2]
        if (self.dp[i] == None):
            self.dp[i] = self.jobs[i][2]
            low, high = i + 1, n
            while (low <= high):
                mid = low + ((high - low) // 2)
                if (self.jobs[mid][0] >= self.jobs[i][1]):
                    self.dp[i] = max(self.dp[i], (self.jobs[i][2] + self.__job_scheduling_helper(mid, n)))
                    high = mid - 1
                else: low = mid + 1
            self.dp[i] = max(self.dp[i], self.__job_scheduling_helper(i + 1, n))
        return self.dp[i]

    def jobScheduling (self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        self.jobs = [(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]
        self.jobs.sort(key=(lambda x : x[0]))
        self.dp = [None for i in range(len(self.jobs))]
        return self.__job_scheduling_helper(0, len(self.jobs) - 1)
