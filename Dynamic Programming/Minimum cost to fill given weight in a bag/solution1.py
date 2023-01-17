from math import inf
class Solution:
    def __min_cost_helper (self, i, w, cost, n):
        if (w == 0): return 0
        if (i == n + 1): return inf
        if (self.dp[w][i] == None):
            self.dp[w][i] = inf
            if (i <= w):
                if (cost[i - 1] != -1):
                    self.dp[w][i] = min(self.dp[w][i],
                                        (cost[i - 1] +
                                         self.__min_cost_helper(i + 1, w - i, cost, n)),
                                        (cost[i - 1] +
                                         self.__min_cost_helper(i, w - i, cost, n)))
                self.dp[w][i] = min(self.dp[w][i], self.__min_cost_helper(i + 1, w, cost, n))
        return self.dp[w][i]

    def minimumCost (self, cost, n, w):
        self.dp = [[None for i in range(len(cost) + 1)] for j in range(w + 1)]
        res = self.__min_cost_helper(1, w, cost, len(cost))
        return res if (res != inf) else -1
