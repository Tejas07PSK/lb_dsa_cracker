from math import inf

class Solution:
    def __edit_helper (self, i, j, word1, word2):
        if (i == len(word1)): return (len(word2) - j)
        if (j == len(word2)): return (len(word1) - i)
        if (self.dp[j][i] == inf):
            if (word1[i] == word2[j]):
                self.dp[j][i] = self.__edit_helper(i + 1, j + 1, word1, word2)
            else:
                self.dp[j][i] = 1 + min(self.__edit_helper(i + 1, j + 1, word1, word2),
                                        self.__edit_helper(i, j + 1, word1, word2),
                                        self.__edit_helper(i + 1, j, word1, word2))
        return self.dp[j][i]

    def minDistance (self, word1: str, word2: str) -> int:
        self.dp = [[inf for j in range(len(word1))] for i in range(len(word2))]
        return self.__edit_helper(0, 0, word1, word2)
