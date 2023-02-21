class Solution:
    def findPosition (self, N):
        if (N == 0): return -1
        if ((N & -N) != N): return -1
        count = 1
        while (N != 1): N, count = N >> 1, count + 1
        return count
