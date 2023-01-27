class Solution:
    def equalPartition (self, n, arr):
        s = sum(arr)
        if ((s % 2) != 0): return 0
        s //= 2
        dp = [[(0 if (i != 0) else int((j - arr[i]) == 0)) for j in range(s + 1)] for i in range(2)]
        for i in range(1, n):
            for j in range(1, s + 1):
                dp[1][j] = 0
                if (j - arr[i] >= 0): dp[1][j] = dp[0][j - arr[i]]
                if (dp[1][j] == 0): dp[1][j] = dp[0][j]
            dp[0], dp[1] = dp[1], dp[0]
        return dp[0][s]
