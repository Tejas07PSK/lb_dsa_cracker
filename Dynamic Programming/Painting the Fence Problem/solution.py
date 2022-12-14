class Solution:
    def countWays (self, n, k):
        if (n == 1): return k
        mod = 1000000007
        same = k * 1
        different =  k * (k - 1)
        tot = same + different
        for i in range(3, n + 1):
            same = different * 1
            different =  (tot * (k - 1)) % mod
            tot = (same + different) % mod
        return tot
