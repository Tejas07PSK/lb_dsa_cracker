class Solution:
    def countBT (self, height):
        mod = 1000000007
        a, b = 1, 1
        for i in range(2, height + 1):
            temp = (((2 * a * b) % mod) + ((a * a) % mod)) % mod
            a, b = temp, a
        return a
