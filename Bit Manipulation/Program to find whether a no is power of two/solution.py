class Solution:
    def isPowerofTwo (self, n):
        if (n == 0): return False
        return True if ((n & -n) == n) else False
