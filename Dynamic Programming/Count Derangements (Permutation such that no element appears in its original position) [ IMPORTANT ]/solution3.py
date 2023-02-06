class Solution:
    def disarrange (self, N):
        mod = 1000000007
        prev_1, prev_2 = 0, 1
        for i in range(3, N + 1):
            temp = prev_2
            prev_2 = ((i - 1) * (prev_2 + prev_1)) % mod
            prev_1 = temp
        return prev_2
