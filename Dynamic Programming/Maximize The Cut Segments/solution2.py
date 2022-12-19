class Solution:
    def maximizeTheCuts (self, n, x, y, z):
        cuts = [x, y, z]
        dp = [0 for i in range(n + 1)]
        for num in range(n + 1):
            for cut in cuts:
                temp = 0
                if ((num - cut) >= 0):
                    temp = 1
                    if ((num - cut) != 0):
                        rest = dp[num - cut]
                        if (rest != 0): temp += rest
                        else: temp = 0
                dp[num] = max(dp[num], temp)
        return dp[n]
