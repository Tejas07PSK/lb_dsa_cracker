class Solution:
    def findElements (self, arr, n, k):
        hm = {}
        for num in arr:
            if (num in hm):
                hm[num] += 1
            else:
                if (len(hm) != (k - 1)):
                    hm[num] = 1
                else:
                    for key in hm:
                        hm[key] -= 1
                        if (hm[key] == 0):
                            del hm[key]
        res = []
        for key in hm:
            count = 0
            for num in arr:
               count = (count + 1) if (key == num) else count
            if (count > (n // k)):
                res.append(key)
        return res