class Solution:
    def countSetBits (self, n):
        count = 0
        while (n > 0):
            count += 1 if ((n & 1) == 1) else 0
            n >>= 1
        return count

    def  sortBySetBitCount (self, arr, n):
        arr.sort(key=lambda x : -self.countSetBits(x))
