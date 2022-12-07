class Solution:
    def maxGold (self, n, m, M):
        dp = [[None for j in range(m)] for i in range(n)]
        ans = 0
        for j in range(m - 1, -1, -1):
            for i in range(n - 1, -1, -1):
                dp[i][j] = M[i][j]
                mx_from_lft = 0
                if (j + 1 < m):
                    mx_from_lft = max(mx_from_lft, dp[i][j + 1])
                    if (i - 1 >= 0): mx_from_lft = max(mx_from_lft, dp[i - 1][j + 1])
                    if (i + 1 < n): mx_from_lft = max(mx_from_lft, dp[i + 1][j + 1])
                dp[i][j] += mx_from_lft
                ans = max(ans, dp[i][j])
        return ans
