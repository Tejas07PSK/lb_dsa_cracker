class Solution:
    def rotateArr (self, A, D, N):
        D %= N
        i, j = 0, N - 1
        while (i < j):
            A[i], A[j] = A[j], A[i]
            i += 1 ; j -= 1
        i, j = N - D, N - 1
        while (i < j):
            A[i], A[j] = A[j], A[i]
            i += 1 ; j -= 1
        i, j = 0, N - D - 1
        while (i < j):
            A[i], A[j] = A[j], A[i]
            i += 1 ; j -= 1
