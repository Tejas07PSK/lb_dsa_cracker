class Solution:
    def longestCommonSubstr (self, s1, s2, n, m):
        dp = [[0 for j in range(len(s2) + 1)] for i in range(2)]
        glob_max = 0
        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2) - 1, -1, -1):
                dp[0][j] = 0
                if (s1[i] == s2[j]):
                    dp[0][j] = 1 + dp[1][j + 1]
                    glob_max = max(glob_max, dp[0][j])
            dp[0], dp[1] = dp[1], dp[0]
        return glob_max
