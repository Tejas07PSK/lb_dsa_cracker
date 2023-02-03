class Solution:
    def longestSubsequence (self, arr, n):
        dp = [0 for i in range(len(arr))]
        ans = 0
        for i in range(len(arr) - 1, -1, -1):
            dp[i] = 1
            for j in range(i + 1, len(arr)):
                if (arr[j] > arr[i]): dp[i] = max(dp[i], 1 + dp[j])
            ans = max(ans, dp[i])
        return ans
