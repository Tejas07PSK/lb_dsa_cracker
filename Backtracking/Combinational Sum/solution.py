from collections import deque
class Solution:
    def __combinationSumHelper (self, A, B, i, N, int_list):
        while (((i + 1) < N) and (A[i] == A[i + 1])): i += 1
        curr_count = B // A[i]
        rem = B % A[i]
        for j in range(curr_count):
            int_list.append(A[i]) ; B -= A[i]
        if (B == 0): self.res.append(list(int_list))
        elif (((i + 1) < N) and (B >= A[i + 1])): self.__combinationSumHelper(A, B, (i + 1), N, int_list)
        for k in range(curr_count):
            int_list.pop() ; B += A[i]
            if (((i + 1) < N) and (B >= A[i + 1])): self.__combinationSumHelper(A, B, (i + 1), N, int_list)

    def combinationalSum (self, A, B):
        self.res = [] ; A.sort()
        self.__combinationSumHelper(A, B, 0, len(A), deque())
        return self.res
