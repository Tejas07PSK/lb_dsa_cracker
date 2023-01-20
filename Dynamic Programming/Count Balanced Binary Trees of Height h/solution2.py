class Solution:
    def countBT (self, height):
        mod = 1000000007
        dp = [None for h in range(height + 1)]
        dp[0] = 1
        for i in range(1, height + 1):
            a, b = 0, 0
            if ((i - 1) >= 0): a = dp[i - 1]
            if ((i - 2) >= 0): b = dp[i - 2]
            dp[i] = (((2 * a * b) % mod) + ((a * a) % mod)) % mod
        return dp[height]
