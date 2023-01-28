class Solution:
    def longestPalinSubseq (self, string):
        dp = [[0 for j in range(len(string))] for i in range(2)]
        dp[1][len(string) - 1] = 1
        for i in range(len(string) - 2, -1, -1):
            dp[0][i] = 1
            for j in range(i + 1, len(string)):
                dp[0][j] = 0
                if (string[i] == string[j]): dp[0][j] = 2 + dp[1][j - 1]
                else: dp[0][j] = max(dp[0][j - 1], dp[1][j])
            dp[0], dp[1] = dp[1], dp[0]
        return dp[1][len(string) - 1]
