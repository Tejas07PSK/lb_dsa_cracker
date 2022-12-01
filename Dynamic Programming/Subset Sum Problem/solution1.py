class Solution:
    def __partition_helper (self, i, s, n, arr):
        if (s == 0): return 1
        if (i == 0):
            if ((s - arr[i]) == 0): return 1
            return 0
        if (self.dp[i][s] == None):
            self.dp[i][s] = 0
            if ((s - arr[i]) >= 0): self.dp[i][s] = self.__partition_helper(i - 1, s - arr[i], n, arr)
            if (self.dp[i][s] == 0): self.dp[i][s] = self.__partition_helper(i - 1, s, n, arr)
        return self.dp[i][s]

    def equalPartition (self, n, arr):
        s = sum(arr)
        if ((s % 2) != 0): return 0
        s = s // 2
        self.dp = [[None for j in range(s + 1)] for i in range(n)]
        return self.__partition_helper(n - 1, s, n, arr)
