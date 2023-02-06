class Solution:
    def disarrange (self, N):
        dp = [0 for i in range(N + 1)]
        mod = 1000000007
        dp[1], dp[2] = 0, 1
        for i in range(3, N + 1):
            dp[i] = ((i - 1) * (dp[i - 1] + dp[i - 2])) % mod
        return dp[N]
