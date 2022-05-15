class Solution:
    def findMinSum (self, A, B, N):
        res = 0
        A.sort() ; B.sort()
        for i in range(N):
            res += abs(A[i] - B[i])
        return res
