class Solution:
    def LongestRepeatingSubsequence (self, s):
        dp = [[0 for i in range(len(s) + 1)] for j in range(2)]
        for j in range(len(s) - 1, -1, -1):
            for i in range(len(s) - 1, -1, -1):
                dp[0][i] = 0
                if ((s[i] == s[j]) and (i != j)): dp[0][i] = 1 + dp[1][i + 1]
                else: dp[0][i] = max(dp[1][i], dp[0][i + 1])
            dp[0], dp[1] = dp[1], dp[0]
        return dp[1][0]
