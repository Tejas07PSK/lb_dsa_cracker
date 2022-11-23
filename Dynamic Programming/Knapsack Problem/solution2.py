class Solution:
    def knapSack (self, w, wt, val, n):
        dp = [[-1 for i in range(0, w + 1)] for i in range(n)]
        for i in range(w + 1): dp[0][i] = val[0] if (wt[0] <= i) else 0
        for i in range(1, n):
            dp[i][0] = 0
            for j in range(1, w + 1):
                if (wt[i] <= j): dp[i][j] = max(val[i] + dp[i - 1][j - wt[i]], dp[i - 1][j])
                else: dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]
