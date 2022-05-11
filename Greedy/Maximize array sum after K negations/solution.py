from math import inf
class Solution:
    def maximizeSum (self, A, N, K):
        if (N == 0): return 0
        min_after_negations, min_after_negations_idx = inf, -1
        for i in range(N):
            if (K == 0): break
            if (A[i] < 0): A[i], K = -A[i], K - 1
            if (A[i] < min_after_negations): min_after_negations, min_after_negations_idx = A[i], i
        if ((K != 0) and ((K % 2) != 0)): A[min_after_negations_idx] = -A[min_after_negations_idx]
        return sum(A)
