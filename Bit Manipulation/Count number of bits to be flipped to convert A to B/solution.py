class Solution:
    def countBitsFlip (self, a, b):
        xor = a ^ b
        count = 0
        while (xor > 0):
            count += 1
            xor -= (xor & -xor)
        return count
