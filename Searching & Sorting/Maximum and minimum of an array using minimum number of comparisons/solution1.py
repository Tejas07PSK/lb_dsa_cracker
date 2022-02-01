class Solution:
    def getMinMax (self, A, N):
        min_ele, max_ele = A[0], A[0]
        for i in range(1, N):
            if (A[i] > max_ele):
                max_ele = A[i]
            elif (A[i] < min_ele):
                min_ele = A[i]
        return min_ele, max_ele
