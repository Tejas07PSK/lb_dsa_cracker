from typing import List
from math import inf

class Solution:
    def maxProfit(self, n: int, prices: List[int]) -> int:
        last_buy = inf
        max_prft = 0
        prfts_from_left = [0 for i in range(n + 1)]
        for i in range(n):
            if (prices[i] < last_buy): last_buy = prices[i]
            if (prices[i] > last_buy): max_prft = max(max_prft, prices[i] - last_buy)
            prfts_from_left[i] = max_prft
        ans = max_prft
        last_sell = -inf
        max_prft = 0
        for i in range(n - 1, -1, -1):
            if (prices[i] > last_sell): last_sell = prices[i]
            if (prices[i] < last_sell): max_prft = max(max_prft, (last_sell - prices[i]))
            ans = max(ans, max_prft, prfts_from_left[i - 1] + max_prft)
        return ans
