def countSubsequences (arr, n, p):
    dp = [[0 for product in range(p + 1)] for item in range(2)]
    for i in range(n - 1, -1, -1):
        for product in range(p, 0, -1):
            dp[i][product] = 0
            if ((arr[i] * product) <= p):
                dp[0][product] = (1 + dp[1][arr[i] * product]) % 1000000007
            dp[0][product] = (dp[0][product] + dp[1][product]) % 1000000007
        dp[0], dp[1] = dp[1], dp[0]
    return dp[1][1]
