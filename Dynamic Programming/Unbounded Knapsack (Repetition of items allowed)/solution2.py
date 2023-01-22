class Solution:
    def knapSack (self, n, w, val, wt):
        dp = [[0 for j in range(w + 1)] for i in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(1, w + 1):
                if ((j - wt[i]) >= 0):
                    dp[i][j] = val[i] + dp[i][j - wt[i]]
                dp[i][j] = max(dp[i][j], dp[i + 1][j])
        return dp[0][w]
