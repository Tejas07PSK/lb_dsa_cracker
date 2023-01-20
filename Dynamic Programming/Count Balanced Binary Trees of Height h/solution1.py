class Solution:
    def __count_bbt_helper (self, height):
        if (height == 0): return 1
        if (self.dp[height] == None):
            self.dp[height] = 0
            a, b = 0, 0
            if ((height - 1) >= 0): a = self.__count_bbt_helper(height - 1)
            if ((height - 2) >= 0): b = self.__count_bbt_helper(height - 2)
            self.dp[height] = (((2 * a * b) % self.mod) + ((a * a) % self.mod)) % self.mod
        return self.dp[height]

    def countBT (self, height):
        self.mod = 1000000007
        self.dp = [None for h in range(height + 1)]
        return self.__count_bbt_helper(height)
