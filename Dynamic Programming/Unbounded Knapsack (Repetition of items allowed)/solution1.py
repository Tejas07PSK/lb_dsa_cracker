class Solution:
    def __knap_sack_helper (self, i, w, n, val, wt):
        if ((i == n) or (w == 0)): return 0
        if (self.dp[i][w] == None):
            self.dp[i][w] = 0
            if ((w - wt[i]) >= 0):
                self.dp[i][w] = val[i] + self.__knap_sack_helper(i, w - wt[i], n, val, wt)
            self.dp[i][w] = max(self.dp[i][w], self.__knap_sack_helper(i + 1, w, n, val, wt))
        return self.dp[i][w]

    def knapSack (self, n, w, val, wt):
        self.dp = [[None for j in range(w + 1)] for i in range(n + 1)]
        return self.__knap_sack_helper(0, w, n, val, wt)
