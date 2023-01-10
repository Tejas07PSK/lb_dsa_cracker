from math import inf
class Solution:
    def eggDrop (self, n, k):
        dp = [[0 for j in range(k + 1)] for i in range(n + 1)]
        for j in range(k + 1): dp[1][j] = j
        for i in range(2, (n + 1)): dp[i][1] = 1
        for i in range(2, (n + 1)):
            for j in range(2, (k + 1)):
                dp[i][j] = inf
                for l in range(1, j + 1):
                    dp[i][j] = min(dp[i][j], max(dp[i][j - l], dp[i - 1][l - 1]))
                dp[i][j] += 1
        return dp[n][k]
