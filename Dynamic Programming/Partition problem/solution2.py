class Solution:
    def equalPartition (self, n, arr):
        s = sum(arr)
        if ((s % 2) != 0): return 0
        s //= 2
        dp = [[(0 if (i != 0) else int((j - arr[i]) == 0)) for j in range(s + 1)] for i in range(n)]
        for i in range(1, n):
            for j in range(1, s + 1):
                if (j - arr[i] >= 0): dp[i][j] = dp[i - 1][j - arr[i]]
                if (dp[i][j] == 0): dp[i][j] = dp[i - 1][j]
        return dp[n - 1][s]
