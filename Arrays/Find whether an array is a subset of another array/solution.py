class Solution:
    def isSubset (self, a1, a2, n, m):
        a1_set = set(a1)
        res = "Yes"
        for number in a2:
            if (number not in a1_set):
                res = "No"
                break
        return res
