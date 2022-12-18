class Solution:
    def __cut_helper(self, n):
        if (self.dp[n] == None):
            #print("IN")
            self.dp[n] = 0
            for cut in self.cuts:
                temp = 0
                if ((n - cut) >= 0):
                    temp = 1
                    if ((n - cut) != 0): temp += self.__cut_helper(n - cut)
                self.dp[n] = max(self.dp[n], temp)
        return self.dp[n]

    def maximizeTheCuts (self, n, x, y, z):
        self.cuts = [x, y, z]
        self.dp = [None for i in range(n + 1)]
        res = self.__cut_helper(n)

print(Solution().maximizeTheCuts(100, 7, 12, 19))
