from math import inf
class Solution:
    def __isPalindrome (self, i, j, string):
        while (i < j):
            if (string[i] != string[j]): return False
            i, j = i + 1, j - 1
        return True

    def __palin_part_helper (self, i, j, string):
        if (i >= j): return 0
        if (self.__isPalindrome(i, j, string)): return 0
        if (self.dp[i][j] == None):
            self.dp[i][j] = inf
            for p in range(i, j + 1):
                left = self.dp[i][p] if (self.dp[i][p] != None) else self.__palin_part_helper(i, p, string)
                right = self.dp[p + 1][j] if (self.dp[p + 1][j] != None) else self.__palin_part_helper(p + 1, j, string)
                self.dp[i][j] = min(self.dp[i][j], (1 + left + right))
        return self.dp[i][j]

    def palindromicPartition (self, string):
        n = len(string)
        self.dp = [[None for j in range(n + 1)] for i in range(n + 1)]
        return self.__palin_part_helper(0, n - 1, string)
