class Solution:
    def lcs (self, x, y, str1, str2):
        dp = [[0 for i in range(len(str1) + 1)] for j in range(2)]
        for j in range(len(str2) - 1, -1, -1):
            for i in range(len(str1) - 1, -1, -1):
                if (str1[i] == str2[j]): dp[0][i] = 1 + dp[1][i + 1]
                else: dp[0][i] = max(dp[1][i], dp[0][i + 1])
            dp[0], dp[1] = dp[1], dp[0]
        return dp[1][0]
