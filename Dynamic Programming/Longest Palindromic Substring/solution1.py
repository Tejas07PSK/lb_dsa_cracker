class Solution:
    def __count_palin_substr_helper (self, i, j, string):
        if (i > j): return True
        if (i == j):
            if (1 > (self.ans[1] - self.ans[0])):
                self.ans[0], self.ans[1] = i, j + 1
            if ((1 == (self.ans[1] - self.ans[0])) and (i < self.ans[0])):
                self.ans[0], self.ans[1] = i, j + 1
            return True
        if (self.dp[i][j] == None):
            self.dp[i][j] = False
            if ((string[i] == string[j]) and (self.__count_palin_substr_helper(i + 1, j - 1, string))):
                self.dp[i][j] = True
                if ((j - i + 1) > (self.ans[1] - self.ans[0])):
                    self.ans[0], self.ans[1] = i, j + 1
                if (((j - i + 1) == (self.ans[1] - self.ans[0])) and (i < self.ans[0])):
                    self.ans[0], self.ans[1] = i, j + 1
            self.__count_palin_substr_helper(i, j - 1, string)
            self.__count_palin_substr_helper(i + 1, j, string)
        return self.dp[i][j]

    def longestPalindrome (self, string):
        self.dp = [[None for j in range(len(string))] for i in range(len(string))]
        self.ans = [0, 0]
        self.__count_palin_substr_helper(0, len(string) - 1, string)
        return string[self.ans[0]:self.ans[1]]
