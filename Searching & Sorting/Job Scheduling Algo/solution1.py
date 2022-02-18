class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit)) ; jobs.sort(key=lambda x : x[1]) ; N = len(jobs)
        profit_calc_arr = [0 for i in range(N)] ;  profit_calc_arr[0] = jobs[0][2]
        for i in range(1, N):
            profit_calc_arr[i] = jobs[i][2]
            for j in range(i - 1, -1, -1):
                if (jobs[j][1] <= jobs[i][0]):
                    profit_calc_arr[i] += profit_calc_arr[j] ; break
            profit_calc_arr[i] = max(profit_calc_arr[i], profit_calc_arr[i - 1])
        return profit_calc_arr[-1]
