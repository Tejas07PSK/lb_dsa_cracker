class Solution:
    def wildCard (self, pattern, text):
        n, m = len(pattern), len(text)
        dp = [[False for j in range(m + 1)] for i in range(n + 1)]
        dp[n][m] = True
        i = n - 1
        while (i >= 0):
            if (pattern[i] == '*'):
                dp[i][m] = dp[i + 1][m]
            i -= 1
        i = n - 1
        while (i >= 0):
            j = m - 1
            while (j >= 0):
                if (pattern[i] == '*'):
                    dp[i][j] = dp[i][j + 1] or dp[i + 1][j]
                elif (pattern[i] == '?') or (pattern[i] == text[j]):
                    dp[i][j] = dp[i + 1][j + 1]
                j -= 1
            i -= 1
        return int(dp[0][0])
