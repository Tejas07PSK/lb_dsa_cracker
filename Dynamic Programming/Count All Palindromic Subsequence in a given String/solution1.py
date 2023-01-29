class Solution:
    def __count_palin_subseq_helper (self, i, j, string):
        if (i > j): return 0
        if (i == j): return 1
        if (self.dp[i][j] == None):
            self.dp[i][j] = 0
            self.dp[i][j] += (self.__count_palin_subseq_helper(i, j - 1, string) +
                              self.__count_palin_subseq_helper(i + 1, j, string))
            if (string[i] == string[j]): self.dp[i][j] += 1
            else: self.dp[i][j] -= self.__count_palin_subseq_helper(i + 1, j - 1, string)
            self.dp[i][j] %= self.mod
        return self.dp[i][j]

    def countPS (self, string):
        self.dp = [[None for j in range(len(string))] for i in range(len(string))]
        self.mod = 1000000007
        return self.__count_palin_subseq_helper(0, len(string) - 1, string)
