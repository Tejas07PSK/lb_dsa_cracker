class Solution:
    def countFriendsPairings (self, n):
        if (n == 0): return 0
        if (n == 1): return 1
        dp = [0 for i in range(n + 1)]
        mod = 1000000007
        dp[0], dp[1], dp[2] = 0, 1, 2
        for i in range(3, n + 1): dp[i] = (dp[i - 1] + (i - 1) * dp[i - 2]) % mod
        return dp[n]
