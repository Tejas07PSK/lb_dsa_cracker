class Solution:
    def __helper__ (self, N):
        if (N == 1): return 0
        if (N == 2): return 1
        if (self.dp[N] == None):
            self.dp[N] = ((N - 1) * (self.__helper__(N - 1) + self.__helper__(N - 2))) % self.mod
        return self.dp[N]

    def disarrange (self, N):
        self.dp = [None for i in range(N + 1)]
        self.mod = 1000000007
        return self.__helper__(N)
