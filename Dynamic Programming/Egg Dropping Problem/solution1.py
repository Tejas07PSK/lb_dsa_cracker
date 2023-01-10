from math import inf
class Solution:
    def __egg_drop_helper (self, n, k):
        if ((n == 0) or (k == 0)): return 0
        if (n == 1): return k
        if (k == 1): return 1
        if (self.dp[n][k] == None):
            self.dp[n][k] = inf
            for i in range(1, k + 1):
                self.dp[n][k] = min(self.dp[n][k], max(self.__egg_drop_helper(n, k - i), self.__egg_drop_helper(n - 1, i - 1)))
            self.dp[n][k] += 1
        return self.dp[n][k]

    def eggDrop (self, n, k):
        self.dp = [[None for j in range(k + 1)] for i in range(n + 1)]
        return self.__egg_drop_helper(n, k)
