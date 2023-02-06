class Solution:
    def findWinner (self, N, X, Y):
        dp = [False for i in range(N + 1)]
        dp[0], dp[1] = False, True
        for i in range(2, N + 1):
            if ((i >= 1) and (not dp[i - 1])): dp[i] = True
            elif ((i >= X) and (not dp[i - X])): dp[i] = True
            elif ((i >= Y) and (not dp[i - Y])): dp[i] = True
        return int(dp[N])
