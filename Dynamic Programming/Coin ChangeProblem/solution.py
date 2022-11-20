class Solution:
    def __coin_change_helper (self, index, target):
        if (target == 0): return 1
        if (self.dp[index][target] == -1):
            self.dp[index][target] = 0
            for i in range(index, len(self.coins)):
                if (self.coins[i] <= target): self.dp[index][target] += self.__coin_change_helper(i, target - self.coins[i])
        return self.dp[index][target]

    def count (self, coins, n, target):
        self.coins = coins
        self.dp = [[-1 for i in range(0, target + 1)] for i in range(n)]
        return self.__coin_change_helper(0, target)
