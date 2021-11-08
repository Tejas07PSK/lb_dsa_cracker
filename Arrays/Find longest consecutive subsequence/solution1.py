class Solution:
    def findLongestConseqSubseq (self, arr, n):
        arr.sort()
        curr_len = 1
        res = 0
        for i in range(1, n):
            if (arr[i] == arr[i - 1]):          # Handle duplicates
                continue
            if (arr[i] != (arr[i - 1] + 1)):    # When a consecutive sub sequence ends
                res = max(res, curr_len)
                curr_len = 1
            else:                               # When we are in a consecutive sub sequence
                curr_len += 1
        res = max(res, curr_len)
        return res
