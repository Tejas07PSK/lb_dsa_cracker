class Solution:
    def __find_max_sum_helper (self, i, arr, n):
        if (i >= n): return 0
        if (self.dp[i] == None):
            self.dp[i] = 0
            if ((i + 1) < n):
                self.dp[i] = max(self.dp[i], (arr[i] + arr[i + 1] + self.__find_max_sum_helper(i + 3, arr, n)))
            self.dp[i] = max(self.dp[i], (arr[i] + self.__find_max_sum_helper(i + 2, arr, n)))
            self.dp[i] = max(self.dp[i], self.__find_max_sum_helper(i + 1, arr, n))
        return self.dp[i]

    def findMaxSum (self, arr, n):
        self.dp = [None for i in range(n)]
        return self.__find_max_sum_helper(0, arr, n)
