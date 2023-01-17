from math import inf
class Solution:
    def minimumCost (self, cost, n, wt):
        dp = [[inf for w in range(wt + 1)] for i in range(2)]
        for i in range(n, 0, -1):
            dp[0][0] = 0
            for w in range(1, wt + 1):
                dp[0][w] = inf
                if (i <= w):
                    if (cost[i - 1] != -1):
                        dp[0][w] = min(dp[0][w], 
                                       (cost[i - 1] + dp[1][w - i]),
                                       (cost[i - 1] + dp[0][w - i]))
                    dp[0][w] = min(dp[0][w], dp[1][w])
            dp[0], dp[1] = dp[1], dp[0]
        return dp[1][wt] if (dp[1][wt] != inf) else -1
