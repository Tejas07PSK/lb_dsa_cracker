def __count_subseq_helper (i, product, arr, n, p, dp):
    if (i == n): return 0
    if (dp[i][product] == None):
        dp[i][product] = 0
        if ((arr[i] * product) <= p):
            dp[i][product] = (1 + __count_subseq_helper(i + 1, (arr[i] * product), arr, n, p, dp)) % 1000000007
        dp[i][product] = (dp[i][product] + __count_subseq_helper(i + 1, product, arr, n, p, dp)) % 1000000007
    return dp[i][product]

def countSubsequences (arr, n, p):
    dp = [[None for product in range(p + 1)] for item in range(len(arr) + 1)]
    return __count_subseq_helper(0, 1, arr, len(arr), p, dp)
