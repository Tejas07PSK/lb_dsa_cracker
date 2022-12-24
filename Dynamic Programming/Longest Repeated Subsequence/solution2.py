class Solution:
    def LongestRepeatingSubsequence (self, s):
        dp = [[0 for j in range(len(s) + 1)] for i in range(len(s) + 1)]
        for j in range(len(s) - 1, -1, -1):
            for i in range(len(s) - 1, -1, -1):
                if ((s[i] == s[j]) and (i != j)): dp[j][i] = 1 + dp[j + 1][i + 1]
                else: dp[j][i] = max(dp[j + 1][i], dp[j][i + 1])
        return dp[0][0]
