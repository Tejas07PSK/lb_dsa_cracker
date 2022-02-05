class Solution:
    def FindMaxSum (self, arr, n):
        if (n == 0):
            return 0
        if (n == 1):
            return arr[0]
        incl_excl = [[0 for i in range(n)] for j in range(2)]
        incl_excl[0][0] = arr[0]
        incl_excl[1][0] = 0
        for i in range(1, n):
            incl_excl[0][i] = arr[i] + incl_excl[1][i - 1]
            incl_excl[1][i] = max(incl_excl[0][i - 1], incl_excl[1][i - 1])
        return max(incl_excl[0][n - 1], incl_excl[1][n - 1])
