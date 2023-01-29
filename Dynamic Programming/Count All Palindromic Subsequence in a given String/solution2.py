class Solution:
    def countPS (self, string):
        dp = [[0 for j in range(len(string))] for i in range(len(string))]
        mod = 1000000007
        for i in range(len(string) - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, len(string)):
                dp[i][j] = dp[i][j - 1] + dp[i + 1][j]
                if (string[i] == string[j]): dp[i][j] += 1
                else: dp[i][j] -= dp[i + 1][j - 1]
                dp[i][j] %= mod
        return dp[0][len(string) - 1]
