class Solution:
    def optimalStrategyOfGame (self, arr, N):
        dp = [[0 for i in range(N + 1)] for j in range(3)]
        for i in range(N - 1, -1, -1):
            dp[0][i] = arr[i]
            for j in range(i + 1, N):
                take_left = arr[i] + min(dp[2][j], dp[1][j - 1])
                take_right = arr[j] + min(dp[0][j - 2], dp[1][j - 1])
                dp[0][j] = max(take_left, take_right)
            dp[1], dp[2] = dp[2], dp[1]
            dp[0], dp[1] = dp[1], dp[0]
        return dp[1][-2]
