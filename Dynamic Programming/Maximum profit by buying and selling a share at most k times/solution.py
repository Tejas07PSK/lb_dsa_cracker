class Solution:
    def maxProfit(self, K, N, A):
        dp = [[0 for i in range(N)] for j in range(K + 1)]
        for i in range(1, K + 1):
            mx_diff = -A[0]
            for j in range(1, N):
                dp[i][j] = max(dp[i][j - 1], A[j] + mx_diff)
                mx_diff = max(mx_diff, dp[i - 1][j] - A[j])
        return dp[-1][-1]
