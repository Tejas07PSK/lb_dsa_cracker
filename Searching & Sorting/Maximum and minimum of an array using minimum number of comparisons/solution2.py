class Solution:
    def __recursiveHelper (self, A, left, right):
        size = right - left + 1
        if (size == 1):
            return A[left], A[left]
        if (size == 2):
            if (A[left] > A[right]):
                return A[right], A[left]
            return A[left], A[right]
        mid = left + ((right - left) // 2)
        min_left, max_left = self.__recursiveHelper(A, left, mid)
        min_right, max_right = self.__recursiveHelper(A, (mid + 1), right)
        return min(min_left, min_right), max(max_left, max_right)

    def getMinMax (self, A, N):
        return self.__recursiveHelper(A, 0, (N - 1))
