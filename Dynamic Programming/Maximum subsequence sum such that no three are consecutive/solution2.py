class Solution:
    def findMaxSum (self, arr, n):
        dp = [0 for i in range(n + 3)]
        for i in range(n - 1, -1, -1):
            if ((i + 1) < n):
                dp[i] = max(dp[i], (arr[i] + arr[i + 1] + dp[i + 3]))
            dp[i] = max(dp[i], (arr[i] + dp[i + 2]))
            dp[i] = max(dp[i], dp[i + 1])
        return dp[0]
