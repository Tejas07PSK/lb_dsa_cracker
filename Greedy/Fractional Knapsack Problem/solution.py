class Solution:
    def fractionalknapsack (self, w, items, n):
        items.sort(key=lambda x: (x.value / x.weight), reverse=True)
        rem_weight, total_profit = w, 0.0
        for item in items:
            if (item.weight <= rem_weight):
                total_profit += item.value ; rem_weight -= item.weight
            else:
                total_profit += (rem_weight * (item.value / item.weight)) ; rem_weight -= rem_weight
            if (rem_weight == 0): break
        return total_profit
