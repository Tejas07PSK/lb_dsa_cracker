class Solution:
    def longestSubsequence (self, arr, n):
        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
        for j in range(n - 1, -1, -1):
            for i in range(n - 1, -2, -1):
                dp[j][i] = 0
                if ((i == -1) or (arr[j] > arr[i])): dp[j][i] = 1 + dp[j + 1][j]
                dp[j][i] = max(dp[j][i], dp[j + 1][i])
        return dp[0][-1]
