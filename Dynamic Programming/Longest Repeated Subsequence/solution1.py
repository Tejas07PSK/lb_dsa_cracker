class Solution:
    def __lrs_helper (self, i, j, s):
        if ((i == len(s)) or (j == len(s))): return 0
        if (self.dp[j][i] == None):
            self.dp[j][i] = 0
            if ((s[i] == s[j]) and (i != j)):
                self.dp[j][i] = 1 + self.__lrs_helper(i + 1, j + 1, s)
            else:
                self.dp[j][i] = max(self.__lrs_helper(i, j + 1, s),
                                    self.__lrs_helper(i + 1, j, s))
        return self.dp[j][i]

    def LongestRepeatingSubsequence (self, s):
        self.dp = [[None for j in range(len(s))] for i in range(len(s))]
        return self.__lrs_helper(0, 0, s)
