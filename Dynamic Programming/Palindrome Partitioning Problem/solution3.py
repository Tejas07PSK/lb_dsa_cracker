from math import inf
class Solution:
    def palindromicPartition (self, string):
        palin = [[False for j in range(len(string))] for i in range(len(string))]
        for i in range(len(string) - 1, -1, -1):
            palin[i][i] = True
            for j in range(i + 1, len(string)):
                if ((string[i] == string[j]) and (((j - i + 1) == 2) or palin[i + 1][j - 1])):
                    palin[i][j] = True
        dp = [inf for i in range(len(string) + 1)]
        for i in range(len(string) - 1, -1, -1):
            for j in range(i, len(string)):
                if (palin[i][j] == True):
                    if (j == (len(string) - 1)):
                        dp[i] = 0
                        break
                    dp[i] = min(dp[i], (1 + dp[j + 1]))
        return dp[0]
