class Solution:
    def setSetBit (self, x, y, l, r):
        mask = ((1 << (r - l + 1)) - 1) << (l - 1)
        mask &= y
        x |= mask
        return x
