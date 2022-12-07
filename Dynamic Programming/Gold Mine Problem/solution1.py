class Solution:
    def __max_gold_helper (self, i, j, n, m, M):
        if ((i == n) or (i == -1)): return 0
        if (j == m): return 0
        if (self.dp[i][j] == None):
            self.dp[i][j] = M[i][j] + max(self.__max_gold_helper(i - 1, j + 1, n, m, M),
                                    self.__max_gold_helper(i, j + 1, n, m, M),
                                    self.__max_gold_helper(i + 1, j + 1, n, m, M))
        return self.dp[i][j]

    def maxGold (self, n, m, M):
        self.dp = [[None for j in range(m)] for i in range(n)]
        ans = 0
        for i in range(n):
            if (self.dp[i][0] == None): self.dp[i][0] = self.__max_gold_helper(i, 0, n, m, M)
            ans = max(ans, self.dp[i][0])
        return ans
