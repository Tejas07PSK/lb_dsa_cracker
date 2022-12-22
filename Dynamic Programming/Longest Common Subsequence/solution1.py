class Solution:
    def __lcs_helper (self, i, j, str1, str2):
        if ((i == len(str1)) or (j == len(str2))): return 0
        if (self.dp[j][i] == None):
            self.dp[j][i] = 0
            if (str1[i] == str2[j]):
                self.dp[j][i] = 1 + self.__lcs_helper(i + 1, j + 1, str1, str2)
            else:
                self.dp[j][i] = max(self.__lcs_helper(i, j + 1, str1, str2),
                                    self.__lcs_helper(i + 1, j, str1, str2))
        return self.dp[j][i]

    def lcs (self, x, y, str1, str2):
        self.dp = [[None for i in range(len(str1))] for j in range(len(str2))]
        return self.__lcs_helper(0, 0, str1, str2)
