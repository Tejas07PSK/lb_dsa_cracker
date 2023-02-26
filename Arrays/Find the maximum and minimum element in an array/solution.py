class Solution:
    def findSum (self, A, N):
        mn, mx = A[0], A[0]
        for i in range(1, N): mn, mx = min(mn, A[i]), max(mx, A[i])
        return mn + mx
