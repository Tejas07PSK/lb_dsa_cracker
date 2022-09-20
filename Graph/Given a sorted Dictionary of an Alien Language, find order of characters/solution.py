from collections import defaultdict
class Solution:
    def findOrder (self, dct, n, k):
        adj_lst = defaultdict(lambda : [])
        for i in range(n - 1):
            string_a, string_b = dct[i], dct[i + 1]
            j, k = 0, 0
            while ((i < len(string_a)) and (j < len(string_b))):
                ch_a, ch_b = string_a[i], string_b[j]
                if (ch_a != ch_b):
                    adj_lst[ch_a].append(ch_b)
                    break