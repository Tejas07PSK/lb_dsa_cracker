class Solution:
    def AlternatingaMaxLength (self, arr):
        dp = [[0 for i in range(len(arr))] for j in range(2)]
        ans = 1
        for i in range(len(arr) - 1, -1, -1):
            dp[0][i], dp[1][i] = 1, 1
            for j in range(i + 1, len(arr)):
                if (arr[i] > arr[j]): dp[0][i] = max(dp[0][i], 1 + dp[1][j])
                if (arr[i] < arr[j]): dp[1][i] = max(dp[1][i], 1 + dp[0][j])
            ans = max(dp[0][i], dp[1][i])
        return ans
