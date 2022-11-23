class Solution:
    def nCr (self, n, r):
        if (r > n): return 0
        if (r == n): return 1
        if ((n - r) < r): r = n - r
        dp = [0 for i in range(r + 1)] ; dp[0] = 1
        md = 1000000007
        for i in range(1, (n + 1)):
            for j in range(min(i, r), 0, -1):
                dp[j] = (dp[j] + dp[j - 1]) % md
        return dp[-1]
