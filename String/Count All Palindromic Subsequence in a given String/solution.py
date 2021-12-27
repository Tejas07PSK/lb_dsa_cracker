class Solution:
    def countPs (self, string):
        n, base = len(string), ((10 ** 9) + 7)
        dp = [[0 for j in range(n)] for i in range(n)]
        for offset in range(n):
            i, j = 0, offset
            while ((i < n) and (j < n)):
                if (offset == 0):
                    dp[i][j] = 1
                elif (offset == 1):
                    dp[i][j] = 3 if (string[i] == string[j]) else 2
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i + 1][j]
                    dp[i][j] = (dp[i][j] + 1) if (string[i] == string[j]) else (dp[i][j] - dp[i + 1][j - 1])
                i += 1 ; j += 1
        return (dp[0][n - 1] % base)
