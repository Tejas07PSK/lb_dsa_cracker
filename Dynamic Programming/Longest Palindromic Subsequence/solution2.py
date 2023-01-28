class Solution:
    def longestPalinSubseq (self, string):
        dp = [[(1 if (i == j) else 0) for j in range(len(string))] for i in range(len(string))]
        for i in range(len(string) - 2, -1, -1):
            for j in range(i + 1, len(string)):
                if (string[i] == string[j]): dp[i][j] = 2 + dp[i + 1][j - 1]
                else: dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        return dp[0][len(string) - 1]
