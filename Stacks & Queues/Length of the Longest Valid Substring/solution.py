class Solution:
    def findMaxLen (self, S):
        opn, clo = 0, 0
        i, n = 0, len(S)
        res = 0
        while (i < n):
            if (S[i] == '('): opn += 1
            else: clo += 1
            if (opn == clo): res = max(res, (opn + clo))
            elif (opn < clo): opn, clo = 0, 0
            i += 1
        i, opn, clo = n - 1, 0, 0
        while (i >= 0):
            if (S[i] == '('): opn += 1
            else: clo += 1
            if (opn == clo): res = max(res, (opn + clo))
            elif (opn > clo): opn, clo = 0, 0
            i -= 1
        return res
