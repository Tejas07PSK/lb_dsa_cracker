from math import inf

class Solution:
    def minDistance (self, word1: str, word2: str) -> int:
        dp = [[inf for i in range(len(word1) + 1)] for j in range(len(word2) + 1)]
        for j in range(len(word2) + 1): dp[j][len(word1)] = len(word2) - j
        for i in range(len(word1) + 1): dp[len(word2)][i] = len(word1) - i
        for j in range(len(word2) - 1, -1, -1):
            for i in range(len(word1) - 1, -1, -1):
                if (word1[i] == word2[j]): dp[j][i] = dp[j + 1][i + 1]
                else: dp[j][i] = 1 + min(dp[j + 1][i + 1], dp[j][i + 1], dp[j + 1][i])
        return dp[0][0]
