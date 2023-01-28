class Solution:
    def __longest_palin_subseq_helper (self, i, j, string):
        if (i > j): return 0
        if (i == j): return 1
        if (self.dp[i][j] == None):
            self.dp[i][j] = 0
            if (string[i] == string[j]):
                self.dp[i][j] = 2 + self.__longest_palin_subseq_helper(i + 1, j - 1, string)
            else:
                self.dp[i][j] = max(self.__longest_palin_subseq_helper(i, j - 1, string),
                                    self.__longest_palin_subseq_helper(i + 1, j, string))
        return self.dp[i][j]

    def longestPalinSubseq (self, string):
        self.dp = [[None for j in range(len(string))] for i in range(len(string))]
        return self.__longest_palin_subseq_helper(0, len(string) - 1, string)
