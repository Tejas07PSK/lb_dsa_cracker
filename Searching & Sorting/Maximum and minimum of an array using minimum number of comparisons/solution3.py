class Solution:
    def getMinMax (self, A, N):
        max_ele, min_ele = 0, 0
        i = 0
        if ((N % 2) != 0):
            min_ele, max_ele = A[0], A[0]
            i = 1
        else:
            if (A[0] > A[1]):
                max_ele = A[0]
                min_ele = A[1]
            else:
                max_ele = A[1]
                min_ele = A[0]
            i = 2
        while (i < N):
            if (A[i] > A[i + 1]):
                if (A[i] > max_ele):
                    max_ele = A[i]
                if (A[i + 1] < min_ele):
                    min_ele = A[i + 1]
            else:
                if (A[i] < min_ele):
                    min_ele = A[i]
                if (A[i + 1] > max_ele):
                    max_ele = A[i + 1]
            i += 2
        return min_ele, max_ele
