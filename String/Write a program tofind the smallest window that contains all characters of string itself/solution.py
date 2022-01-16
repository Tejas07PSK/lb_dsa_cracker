import math
class Solution:
    def findSubString (self, string):
        i, j, n = 0, 0, len(string)
        hm = {}
        res = math.inf
        unique_count_in_string = len(set(string))
        while (j < n):
            if string[j] not in hm:
                hm[string[j]] = 0
            hm[string[j]] += 1
            while (len(hm) == unique_count_in_string):
                res = min(res, (j - i + 1))
                hm[string[i]] -= 1
                if (hm[string[i]] == 0):
                    del hm[string[i]]
                i += 1
            j += 1
        return res
