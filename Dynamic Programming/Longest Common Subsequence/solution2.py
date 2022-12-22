class Solution:
    def lcs (self, x, y, str1, str2):
        dp = [[0 for i in range(len(str1) + 1)] for j in range(len(str2) + 1)]
        for j in range(len(str2) - 1, -1, -1):
            for i in range(len(str1) - 1, -1, -1):
                if (str1[i] == str2[j]): dp[j][i] = 1 + dp[j + 1][i + 1]
                else: dp[j][i] = max(dp[j + 1][i], dp[j][i + 1])
        return dp[0][0]
