class Solution:
    def __maximum_amt_helper (self, i, j, arr):
        if (i > j): return 0
        if (i == j): return arr[i]
        if (self.dp[i][j] == None):
            take_left = arr[i] + min(self.__maximum_amt_helper(i + 2, j, arr),
                                     self.__maximum_amt_helper(i + 1, j - 1, arr))
            take_right = arr[j] + min(self.__maximum_amt_helper(i, j - 2, arr),
                                      self.__maximum_amt_helper(i + 1, j - 1, arr))
            self.dp[i][j] = max(take_left, take_right)
        return self.dp[i][j]

    def optimalStrategyOfGame (self, arr, N):
        self.dp = [[None for i in range(N)] for j in range(N)]
        return self.__maximum_amt_helper(0, N - 1, arr)
