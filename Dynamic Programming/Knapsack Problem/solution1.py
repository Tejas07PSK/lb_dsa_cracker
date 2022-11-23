class Solution:
    def __knap_sack_helper (self, index, target):
        if (target == 0): return 0
        if (index == 0): return self.value[0] if (self.weight[0] <= target) else 0
        if (self.dp[index][target] == -1):
            if ((index - 1) >= 0):
                if (self.weight[index] <= target):
                    self.dp[index][target] = self.value[index] + self.__knap_sack_helper(index - 1, target - self.weight[index])
                    self.dp[index][target] = max(self.dp[index][target], self.__knap_sack_helper(index - 1, target))
                else: self.dp[index][target] = self.__knap_sack_helper(index - 1, target)
        return self.dp[index][target]

    def knapSack (self, w, wt, val, n):
        self.weight, self.value = wt, val
        self.dp = [[-1 for i in range(0, w + 1)] for i in range(n)]
        return self.__knap_sack_helper(n - 1, w)
