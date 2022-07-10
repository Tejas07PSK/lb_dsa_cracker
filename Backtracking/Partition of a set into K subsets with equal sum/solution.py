class Solution:
    def __isKPartitionPossibleHelper (self, a, i, sum_so_far, n, k):
        if (k == 0): return True
        if (sum_so_far == self.tot):
            if (self.__isKPartitionPossibleHelper(a, 0, 0, n, k - 1)): return True
            return False
        while ((i < n) and self.taken[i]): i += 1
        if (i == n): return False
        self.taken[i] = True
        if (self.__isKPartitionPossibleHelper(a, i + 1, sum_so_far + a[i], n, k)): return True
        self.taken[i] = False
        if (self.__isKPartitionPossibleHelper(a, i + 1, sum_so_far, n, k)): return True
        return False

    def isKPartitionPossible (self, a, k):
        self.tot = sum(a)
        if ((self.tot % k) != 0): return 0
        self.tot //= k ; self.taken = [False for i in range(len(a))]
        if (self.__isKPartitionPossibleHelper(a, 0, 0, len(a), k)): return 1
        return 0
