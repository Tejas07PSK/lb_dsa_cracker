def maxStock (prices, n, k):
    stock_values_limits, res = [(prices[i], i + 1) for i in range(len(prices))], 0
    stock_values_limits.sort(key=lambda x: x[0])
    for price, limit in stock_values_limits:
        if ((k <= 0) or (price > k)): break
        temp = min(limit, (k // price)) ; res += temp ; k -= (price * temp)
    return res
