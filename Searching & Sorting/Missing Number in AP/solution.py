import math
class Solution:
    def findMissingNumberInAp (self, arr, n):
        cmm_diff = math.ceil((arr[n - 1] - arr[0]) / n)
        low, high, ans = 0, n - 1, 0
        while (low <= high):
            mid = low + ((high - low) // 2) ; act_num = arr[0] + (mid * cmm_diff)
            if (act_num >= arr[mid]):
                low = mid + 1
            else:
                ans = act_num
                high = mid - 1
        return ans
