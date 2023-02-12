from math import inf
class Solution:
    def __optimal_search_tree (self, i, j, keys, freq):
        if (i > j): return 0
        if (i == j): return freq[i]
        if (self.dp[i][j] == None):
            self.dp[i][j] = inf
            for root in range(i, j + 1):
                self.dp[i][j] = min(self.dp[i][j],
                                    (self.__optimal_search_tree(i, root - 1, keys, freq) +
                                     self.__optimal_search_tree(root + 1, j, keys, freq) +
                                     (self.sums[j] - self.sums[i] + freq[i])))
        return self.dp[i][j]

    def optimalSearchTree (self, keys, freq, n):
        self.dp = [[None for j in range(n)] for i in range(n)]
        self.sums = [0 for i in range(n)] ; self.sums[0] = freq[0]
        for i in range(1, n): self.sums[i] = self.sums[i - 1] + freq[i]
        return self.__optimal_search_tree(0, n - 1, keys, freq)
