from typing import List
class Solution:
    def maxProfit (self, n: int, price: List[int]) -> int:
        mn, mx_prft = price[0], 0
        profits_from_left = [0 for i in range(n)]
        for i in range(1, n):
            if (price[i] > mn):
                mx_prft = max(mx_prft, price[i] - mn)
                profits_from_left[i] = mx_prft
            elif (price[i] < mn): mn = price[i]
        mx, mx_prft, ans = price[-1], 0, 0
        for i in range(n - 2, -1, -1):
            if (price[i] < mx):
                prf_till_i = 0 if ((i - 1) == -1) else profits_from_left[i - 1]
                mx_prft = max(mx_prft, mx - price[i])
                profits_from_left[i] = prf_till_i + mx_prft
                ans = max(ans, profits_from_left[i])
            elif (price[i] > mx): mx = price[i]
        return ans
