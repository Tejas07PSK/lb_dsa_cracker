class Solution:
    def AlternatingaMaxLength (self, arr):
        dp = [[0 for i in range(len(arr))] for j in range(2)]
        dp[0][-1], dp[1][-1], ans = 1, 1, 1
        for i in range(len(arr) - 2, -1, -1):
            if (arr[i] > arr[i + 1]):
                dp[0][i] = 1 + dp[1][i + 1]
                dp[1][i] = dp[1][i + 1]
            if (arr[i] < arr[i + 1]):
                dp[1][i] = 1 + dp[0][i + 1]
                dp[0][i] = dp[0][i + 1]
            if (arr[i] == arr[i + 1]):
                dp[0][i], dp[1][i] = dp[0][i + 1], dp[1][i + 1]
        ans = max(dp[0][0], dp[1][0])
        return ans
