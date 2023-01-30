class Solution:
    def longestPalindrome (self, string):
        dp = [[True for j in range(len(string))] for i in range(2)]
        ans = [len(string) - 1, len(string)]
        for i in range(len(string) - 2, -1, -1):
            dp[0][i] = True
            if (1 > (ans[1] - ans[0])): ans[0], ans[1] = i, i + 1
            if ((1 == (ans[1] - ans[0])) and (i < ans[0])): ans[0], ans[1] = i, i + 1
            for j in range(i + 1, len(string)):
                dp[0][j] = False
                if ((string[i] == string[j]) and dp[1][j - 1]):
                    dp[0][j] = True
                    if ((j - i + 1) > (ans[1] - ans[0])): ans[0], ans[1] = i, j + 1
                    if (((j - i + 1) == (ans[1] - ans[0])) and (i < ans[0])): ans[0], ans[1] = i, j + 1
            dp[0], dp[1] = dp[1], dp[0]
        return string[ans[0]:ans[1]]
