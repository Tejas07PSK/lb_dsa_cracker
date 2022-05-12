class Solution:
    def Maximize (self, arr, n):
        idx_val_prod_sum, factor = 0, (10 ** 9 + 7)
        arr.sort()
        for i in range(n):
            idx_val_prod_sum += (arr[i] * i)
        return (idx_val_prod_sum % factor)
