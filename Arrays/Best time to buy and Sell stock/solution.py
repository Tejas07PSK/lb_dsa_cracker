class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_index = 0
        buy_index_min = 0
        sell_index = 1
        sell_index_max = 0
        n = len(prices)
        while (sell_index < n):
            if (prices[sell_index] < prices[buy_index]):
                buy_index = sell_index
                sell_index += 1
                continue
            if ((prices[sell_index] - prices[buy_index]) > (prices[sell_index_max] - prices[buy_index_min])):
                sell_index_max = sell_index
                buy_index_min = buy_index
            sell_index += 1
        return (prices[sell_index_max] - prices[buy_index_min])
