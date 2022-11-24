def P (n, k):
    if (k > n): return 0
    if (k == 0): return 1
    md = 1000000007
    dp = [[0 for i in range(k + 1)] for j in range(2)] ; dp[0][0] = 1
    for i in range(1, n + 1):
        dp[1][0] = 1
        for j in range(1, k + 1): dp[1][j] = (dp[0][j] + (j * dp[0][j - 1])) % md
        dp[0], dp[1] = dp[1], dp[0]
    return dp[0][-1]
