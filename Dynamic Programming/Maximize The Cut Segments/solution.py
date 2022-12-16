class Solution:
    def __cut_helper(self, n):
        if (self.dp[n] == None):
            self.dp[n] = 0
            for cut in self.cuts:
                temp = 0
                a = n // cut
                b =  n % cut
                if (a > 0): temp += a * self.__cut_helper(cut)
                if ((b != 0) and (b != n)): temp += self.__cut_helper(b)
                self.dp[n] = max(self.dp[n], temp)
        return self.dp[n]

    def maximizeTheCuts (self, n, x, y, z):
        self.cuts = [x, y, z]
        self.dp = [None for i in range(1, n + 1)]
        return self.__cut_helper(n)
