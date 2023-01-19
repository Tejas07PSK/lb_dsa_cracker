def count (n):
    arr = [3, 5, 10]
    dp = [[0 for j in range(n + 1)] for i in range(3 + 1)]
    for i in range(2, -1, -1):
        dp[i][0] = 1
        for target in range(1, n + 1, 1):
            dp[i][target] = dp[i + 1][target]
            if ((target - arr[i]) >= 0): dp[i][target] += dp[i][target - arr[i]]
    return dp[0][n]
