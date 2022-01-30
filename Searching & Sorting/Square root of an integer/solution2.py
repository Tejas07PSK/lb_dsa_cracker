class Solution:
    def countSquares (self, x):
        if (x == 1):
            return 0
        left, right = 1, x // 2
        res = 0
        while (left <= right):
            mid = left + ((right - left) // 2)
            pwr = mid * mid
            if (pwr < x):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res
