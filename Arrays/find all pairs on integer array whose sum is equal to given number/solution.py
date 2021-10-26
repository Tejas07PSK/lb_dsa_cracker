class Solution:
    def getPairsCount (self, arr, n, k):
        hm = {}
        res = 0
        diff = 0
        for item in arr:
            if item > k:
                continue
            diff = (k - item)
            if diff in hm.keys():
                res += hm[diff]
            hm[item] = 1 if item not in hm.keys() else (hm[item] + 1)
        return res