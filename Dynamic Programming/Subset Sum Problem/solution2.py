class Solution:
    def equalPartition (self, n, arr):
        s = sum(arr)
        if ((s % 2) != 0): return 0
        s = s // 2
        dp = [[None for j in range(s + 1)] for i in range(2)]
        dp[0][0] = 1
        for j in range(1, s + 1): dp[0][j] = 1 if ((j - arr[0]) == 0) else 0
        for i in range(1, n):
            dp[1][0] = 1
            for j in range(1, s + 1): dp[1][j] = int((dp[0][j - arr[i]] if ((j - arr[i]) >= 0) else 0) or dp[0][j])
            dp[0], dp[1] = dp[1], dp[0]
        return dp[0][-1]
