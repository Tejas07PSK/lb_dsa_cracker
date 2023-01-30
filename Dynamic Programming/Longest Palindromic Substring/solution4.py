class Solution:
    def __palin_expander__ (self, i, j, string, n):
        while ((i >= 0) and (j < n) and (string[i] == string[j])): i, j = i - 1, j + 1
        return i + 1, j - 1

    def longestPalindrome (self, string):
        ans = [0, 0]
        for i in range(len(string)):
            x, y = self.__palin_expander__(i - 1, i + 1, string, len(string))
            if ((y - x + 1) > (ans[1] - ans[0])): ans[0], ans[1] = x, y + 1
            x, y = self.__palin_expander__(i, i + 1, string, len(string))
            if ((y - x + 1) > (ans[1] - ans[0])): ans[0], ans[1] = x, y + 1
        return string[ans[0]:ans[1]]
