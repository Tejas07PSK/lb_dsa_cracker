class Solution:
    def findLongestConseqSubseq (self, arr, n):
        set_of_nos = set(arr)
        res = 0
        for num in arr:
            if ((num - 1) not in set_of_nos):
                curr_len = 1
                while ((num + 1) in set_of_nos):
                    num += 1
                    curr_len += 1
                res = max(res, curr_len)
        return res
