class Solution:
    def __lis_helper (self, i, j, arr):
        if (j == len(arr)): return 0
        if (self.dp[j][i] == None):
            self.dp[j][i] = 0
            if ((i == -1) or (arr[j] > arr[i])):
                self.dp[j][i] = 1 + self.__lis_helper(j, j + 1, arr)
            self.dp[j][i] = max(self.dp[j][i], self.__lis_helper(i, j + 1, arr))
        return self.dp[j][i]

    def longestSubsequence (self, arr, n):
        self.dp = [[None for i in range(n + 1)] for j in range(n + 1)]
        return self.__lis_helper(-1, 0, arr)
