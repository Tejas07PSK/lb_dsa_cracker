class Solution:
    def count (self, coins, n, target):
        dp = [[0 for i in range(0, target + 1)] for i in range(n)]
        for i in range(target + 1):
            dp[0][i] = int((i % coins[0]) == 0)
        for i in range(1, n):
            dp[i][0] = 1
            for j in range(1, target + 1):
                if (coins[i] <= j): dp[i][j] = dp[i][j - coins[i]]
                dp[i][j] += dp[i - 1][j]
        return dp[-1][-1]
