class Solution:
    def longestPalindrome (self, string):
        dp = [[True for j in range(len(string))] for i in range(len(string))]
        ans = [len(string) - 1, len(string)]
        for i in range(len(string) - 2, -1, -1):
            dp[i][i] = True
            if (1 > (ans[1] - ans[0])): ans[0], ans[1] = i, i + 1
            if ((1 == (ans[1] - ans[0])) and (i < ans[0])): ans[0], ans[1] = i, i + 1
            for j in range(i + 1, len(string)):
                dp[i][j] = False
                if ((string[i] == string[j]) and dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if ((j - i + 1) > (ans[1] - ans[0])): ans[0], ans[1] = i, j + 1
                    if (((j - i + 1) == (ans[1] - ans[0])) and (i < ans[0])): ans[0], ans[1] = i, j + 1
        return string[ans[0]:ans[1]]
