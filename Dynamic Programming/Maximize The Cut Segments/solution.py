class Solution:
    def __cut_helper(self, n):
        if (self.dp[n] == None):
            self.dp[n] = 0
            for cut in self.cuts:
                temp = 0
                if ((n - cut) >= 0):
                    temp = 1
                    if ((n - cut) != 0):
                        rest = self.__cut_helper(n - cut)
                        if (rest != 0): temp += rest
                        else: temp = 0
                self.dp[n] = max(self.dp[n], temp)
        return self.dp[n]

    def maximizeTheCuts (self, n, x, y, z):
        self.cuts = [x, y, z] ; self.cuts.sort()
        self.dp = [None for i in range(n + 1)]
        return self.__cut_helper(n)
