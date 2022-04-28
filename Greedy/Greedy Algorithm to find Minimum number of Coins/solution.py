class Solution:
    def minPartition (self, N):
        currency_type_table = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
        rem_total, currency_index, res = N, len(currency_type_table) - 1, []
        while (rem_total > 0):
            while (currency_type_table[currency_index] > rem_total): currency_index -= 1
            res.append(currency_type_table[currency_index]) ; rem_total -= currency_type_table[currency_index]
        return res
