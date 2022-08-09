class Solution:
    def isStackPermutation (self, N, A, B):
        stk, j = [], 0
        for num in A:
            stk.append(num)
            while ((stk) and (stk[-1] == B[j])):
                stk.pop() ; j += 1
        while (stk):
            if (stk[-1] != B[j]): return 0
            stk.pop() ; j += 1
        return 1
