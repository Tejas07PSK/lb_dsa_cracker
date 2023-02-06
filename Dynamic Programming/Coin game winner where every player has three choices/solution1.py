class Solution:
    def __find_winner_helper (self, N, X, Y):
        if (N == 0): return False
        if (N == 1): return True
        if (self.dp[N] == None):
            self.dp[N] = False
            if ((N >= 1) and (not self.__find_winner_helper(N - 1, X, Y))): self.dp[N] = True
            elif ((N >= X) and (not self.__find_winner_helper(N - X, X, Y))): self.dp[N] = True
            elif ((N >= Y) and (not self.__find_winner_helper(N - Y, X, Y))): self.dp[N] = True
        return self.dp[N]

    def findWinner (self, N, X, Y):
        self.dp = [None for i in range(N + 1)]
        return int(self.__find_winner_helper(N, X, Y))
