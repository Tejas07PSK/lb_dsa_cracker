class Solution:
    def optimalStrategyOfGame (self, arr, N):
        dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
        for i in range(N - 1, -1, -1):
            dp[i][i] = arr[i]
            for j in range(i + 1, N):
                take_left = arr[i] + min(dp[i + 2][j], dp[i + 1][j - 1])
                take_right = arr[j] + min(dp[i][j - 2], dp[i + 1][j - 1])
                dp[i][j] = max(take_left, take_right)
        return dp[0][-2]
