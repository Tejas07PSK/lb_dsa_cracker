class Solution:
    def __longest_subseq_helper(self, i, j, arr, n):
        if (j == n): return 0
        if (self.dp[j][i] == None):
            self.dp[j][i] = 0
            if ((i == -1) or (abs(arr[j] - arr[i]) == 1)):
                self.dp[j][i] = 1 + self.__longest_subseq_helper(j, j + 1, arr, n)
            self.dp[j][i] = max(self.dp[j][i], self.__longest_subseq_helper(i, j + 1, arr, n))
        return self.dp[j][i]

    def longestSubseq (self, arr, n):
        self.dp = [[None for i in range(n + 1)] for j in range(n + 1)]
        return self.__longest_subseq_helper(-1, 0, arr, len(arr))
