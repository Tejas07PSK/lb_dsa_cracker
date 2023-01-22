class Solution:
    def knapSack (self, n, w, val, wt):
        dp = [[0 for j in range(w + 1)] for i in range(2)]
        for i in range(n - 1, -1, -1):
            dp[0][0] = 0
            for j in range(1, w + 1):
                dp[0][j] = 0
                if ((j - wt[i]) >= 0): dp[0][j] = val[i] + dp[0][j - wt[i]]
                dp[0][j] = max(dp[0][j], dp[1][j])
            dp[0], dp[1] = dp[1], dp[0]
        return dp[1][w]
