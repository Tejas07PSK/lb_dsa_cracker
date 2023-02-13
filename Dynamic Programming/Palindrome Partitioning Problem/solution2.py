from math import inf
class Solution:
    def __palin_part_helper (self, i, string):
        if (self.dp[i] == None):
            self.dp[i] = inf
            for j in range(i, len(string)):
                if (self.palin[i][j] == True):
                    if (j == (len(string) - 1)):
                        self.dp[i] = 0
                        break
                    self.dp[i] = min(self.dp[i], (1 + self.__palin_part_helper(j + 1, string)))
        return self.dp[i]

    def palindromicPartition (self, string):
        self.palin = [[False for j in range(len(string))] for i in range(len(string))]
        for i in range(len(string) - 1, -1, -1):
            self.palin[i][i] = True
            for j in range(i + 1, len(string)):
                if ((string[i] == string[j]) and (((j - i + 1) == 2) or self.palin[i + 1][j - 1])):
                    self.palin[i][j] = True
        self.dp = [None for i in range(len(string) + 1)]
        return self.__palin_part_helper(0, string)
