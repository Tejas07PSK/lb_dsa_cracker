def countSubsequences (arr, n, p):
    dp = [[0 for product in range(p + 1)] for item in range(len(arr) + 1)]
    for i in range(n - 1, -1, -1):
        for product in range(p, 0, -1):
            if ((arr[i] * product) <= p):
                dp[i][product] = (1 + dp[i + 1][arr[i] * product]) % 1000000007
            dp[i][product] = (dp[i][product] + dp[i + 1][product]) % 1000000007
    return dp[0][1]
