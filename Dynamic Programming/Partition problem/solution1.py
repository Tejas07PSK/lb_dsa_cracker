class Solution:
    def __equal_partition_helper (self, i, j, arr):
        if (j == 0): return 1
        if (i == 0): return int((j - arr[i]) == 0)
        if (self.dp[i][j] == None):
            self.dp[i][j] = 0
            if (j - arr[i] >= 0):
                self.dp[i][j] = self.__equal_partition_helper(i - 1, j - arr[i], arr)
            if (self.dp[i][j] == 0):
                self.dp[i][j] = self.__equal_partition_helper(i - 1, j, arr)
        return self.dp[i][j]

    def equalPartition (self, n, arr):
        s = sum(arr)
        if ((s % 2) != 0): return 0
        s //= 2
        self.dp = [[None for j in range(s + 1)] for i in range(n)]
        return self.__equal_partition_helper(n - 1, s, arr)
