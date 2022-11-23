class Solution:
    def nCr (self, n, r):
        if (r > n): return 0
        if (r == n): return 1
        md = 1000000007
        nmtr, denom, i = 1, 1, 0
        while (i < r):
            nmtr = (nmtr * (n - i))
            i += 1
        i = 1
        while (i <= r):
            denom = (denom * i)
            i += 1
        return ((nmtr // denom) % md)
