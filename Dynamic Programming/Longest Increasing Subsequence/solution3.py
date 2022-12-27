class Solution:
    def longestSubsequence (self, arr, n):
        dp = [[0 for i in range(n + 1)] for j in range(2)]
        for j in range(n - 1, -1, -1):
            for i in range(n - 1, -2, -1):
                dp[0][i] = 0
                if ((i == -1) or (arr[j] > arr[i])): dp[0][i] = 1 + dp[1][j]
                dp[0][i] = max(dp[0][i], dp[1][i])
            dp[0], dp[1] = dp[1], dp[0]
        return dp[1][-1]
