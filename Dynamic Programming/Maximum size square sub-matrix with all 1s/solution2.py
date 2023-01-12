class Solution:
    def maxSquare (self, n, m, mat):
        dp = [[0 for j in range(len(mat[0]) + 1)] for i in range(len(mat) + 1)]
        glob_max = 0
        for i in range(len(mat) - 1, -1, -1):
            for j in range(len(mat[0]) - 1, -1, -1):
                if (mat[i][j] == 1): dp[i][j] = 1 + min(dp[i][j + 1], dp[i + 1][j + 1], dp[i + 1][j])
                glob_max = max(glob_max, dp[i][j])
        return glob_max
