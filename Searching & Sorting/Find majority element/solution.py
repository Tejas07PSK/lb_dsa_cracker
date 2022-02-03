class Solution:
    def majorityElement (self, arr, n):
        m = n // 2
        cand_occr = [arr[0], 1]
        i = 1
        while (i < n):
            if (arr[i] == cand_occr[0]):
                cand_occr[1] += 1
            else:
                cand_occr[1] -= 1
                if (cand_occr[1] == 0):
                    cand_occr[0] = arr[i]
                    cand_occr[1] = 1
            i += 1
        i, cntr = 0, 0
        while (i < n):
            if (arr[i] == cand_occr[0]):
                cntr += 1
                if (cntr > m):
                    return cand_occr[0]
            i += 1
        return -1
