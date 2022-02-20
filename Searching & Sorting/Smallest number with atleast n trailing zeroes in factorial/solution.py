import math
class Solution:
    def findNum (self, N):
        low, high, ans = 1, 5 * N, 0
        while (low <= high):
            mid = low + ((high - low) // 2) ; count_zeroes_in_fact, factor, num = 0, 5, math.floor(mid / 5)
            while (num > 0):
                count_zeroes_in_fact += num ; factor *= 5
                num = math.floor(mid / factor)
            if (count_zeroes_in_fact < N): low = mid + 1
            else:
                ans = mid ; high = mid - 1
        return ans
