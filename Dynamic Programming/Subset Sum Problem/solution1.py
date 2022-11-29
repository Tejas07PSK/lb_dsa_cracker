class Solution:
    def __partition_helper (self, tot, i, s, n, arr):
        if ((s - tot) == tot): return 1
        if (i == n): return 0
        if (self.dp[i][tot] == None):
            self.dp[i][tot] = (self.__partition_helper(tot, i + 1, s, n, arr) or
                               self.__partition_helper(tot + arr[i], i + 1, s, n, arr))
        return self.dp[i][tot]

    def equalPartition (self, n, arr):
        s = sum(arr)
        self.dp = [[None for j in range(s + 1)] for i in rnage(n + 1)]
        return self.__prtiton_helper(0, 0, s, n, arr)
