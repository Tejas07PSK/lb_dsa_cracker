from math import inf
class Solution:
    def optimalSearchTree (self, keys, freq, n):
        dp = [[0 for j in range(n + 1)] for i in range(n + 1)]
        sums = [0 for i in range(n + 1)]
        for i in range(n): sums[i] = sums[i - 1] + freq[i]
        for i in range(n - 1, -1, -1):
            dp[i][i] = freq[i]
            for j in range(i + 1, n):
                dp[i][j] = inf
                for root in range(i, j + 1):
                    dp[i][j] = min(dp[i][j], (dp[i][root - 1] + dp[root + 1][j] + (sums[j] - sums[i] + freq[i])))
        return dp[0][-2]
