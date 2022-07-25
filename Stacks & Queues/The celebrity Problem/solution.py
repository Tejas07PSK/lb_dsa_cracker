class Solution:
    def celebrity (self, M, n):
        i, j = 0, n - 1
        while (i != j):
            if (M[i][j] == 1): i += 1
            else: j -= 1
        for k in range(i + 1, n):
            if (M[k][i] != 1): return -1
        for k in range(0, n):
            if (M[i][k] != 0): return -1
        return i
