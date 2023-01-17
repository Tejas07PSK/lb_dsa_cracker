from math import inf
class Solution:
    def minimumCost (self, cost, n, wt):
        dp = [[(0 if ((w == 0) and (i != (n + 1))) else inf) for w in range(wt + 1)] for i in range(len(cost) + 2)]
        for i in range(n, 0, -1):
            for w in range(1, wt + 1):
                if (i <= w):
                    if (cost[i - 1] != -1):
                        dp[i][w] = min(dp[i][w], 
                                       (cost[i - 1] + dp[i + 1][w - i]),
                                       (cost[i - 1] + dp[i][w - i]))
                    dp[i][w] = min(dp[i][w], dp[i + 1][w])
        return dp[1][wt] if (dp[1][wt] != inf) else -1
