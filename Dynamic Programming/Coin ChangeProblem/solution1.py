class Solution:
    def __coin_change_helper (self, index, target):
        if (target == 0): return 1
        if (index == 0): return int((target % self.coins[index]) == 0)
        if (self.dp[index][target] == -1):
            self.dp[index][target] = 0
            if (self.coins[index] <= target):
                self.dp[index][target] = self.__coin_change_helper(index, target - self.coins[index])
            if ((index - 1) >= 0):
                self.dp[index][target] += self.__coin_change_helper(index - 1, target)
        return self.dp[index][target]

    def count (self, coins, n, target):
        self.coins = coins
        self.dp = [[-1 for i in range(0, target + 1)] for i in range(n)]
        return self.__coin_change_helper(n - 1, target)
