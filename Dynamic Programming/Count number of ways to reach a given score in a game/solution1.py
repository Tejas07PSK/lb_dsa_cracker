def __helper (i, target, arr, dp):
    if (target == 0): return 1
    if (i == len(arr)): return 0
    if (dp[i][target] == None):
        dp[i][target] = 0
        if ((target - arr[i]) >= 0):
            dp[i][target] = __helper(i + 1, target, arr, dp) + __helper(i, target - arr[i], arr, dp)
    return dp[i][target]

def count (n):
    arr = [3, 5, 10]
    dp = [[None for j in range(n + 1)] for i in range(3)]
    return __helper(0, n, arr, dp)
