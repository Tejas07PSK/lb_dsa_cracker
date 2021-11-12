class Solution:
    def findMinDiff (self, A, N, M):
        A.sort()
        min_diff =  (A[M - 1] - A[0])
        i = M
        while (i < N):
            min_diff = min(min_diff, (A[i] - A[i - M + 1]))
            i += 1
        return min_diff
            