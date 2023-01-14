class Solution:
    def maximumPath (self, n, mat):
        dp = [[0 for j in range(n + 1)] for i in range(2)]
        glob_max = 0
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[0][j] = 0
                dp[0][j] = mat[i][j] + max(dp[1][j], dp[1][j + 1], dp[1][j - 1])
                glob_max = max(glob_max, dp[0][j])
            dp[0], dp[1] = dp[1], dp[0]
        return glob_max
