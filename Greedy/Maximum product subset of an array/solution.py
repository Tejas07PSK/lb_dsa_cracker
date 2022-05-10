from math import inf
class Solution:
    def findMaxProduct (self, arr, n):
        if (n == 0): return 0
        if (n == 1): return arr[0]
        pos_count, neg_count, zero_count = 0, 0, 0
        neg_prod, pos_prod = 1, 1
        largest_among_neg_numbers = -inf
        for i in range(n):
            if (arr[i] < 0): neg_count, largest_among_neg_numbers = neg_count + 1, max(largest_among_neg_numbers, arr[i])
            if (arr[i] > 0): pos_count, pos_prod = pos_count + 1, pos_prod * arr[i]
            if (arr[i] == 0): zero_count += 1
        if (neg_count > 0):
            for i in range(n):
                if (arr[i] < 0):
                    if ((largest_among_neg_numbers != -inf) and (arr[i] == largest_among_neg_numbers) and ((neg_count % 2) != 0)):
                        largest_among_neg_numbers = -inf ; continue
                    neg_prod *= arr[i]
        if (((neg_count == 0) or (neg_count == 1)) and (pos_count == 0) and (zero_count > 0)): return 0
        return ((neg_prod * pos_prod) % (10 ** 9 + 7))
