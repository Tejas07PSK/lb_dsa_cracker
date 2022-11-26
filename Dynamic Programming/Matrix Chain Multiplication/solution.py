class Solution:
    def matrixMultiplication (self, n, arr):
        dp = [[0 for i in range(n - 1)] for j in range(n - 1)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n - 1):
                k, dp[i][j] = i, inf
                while (k < (n - 1)):
                    dp[i][j] = min(dp[i][j], (dp[i][k] + dp[k + 1][j] + (arr[i] * arr[k + 1] * arr[j + 1])))
                    k += 1
        return dp[0][-1]
