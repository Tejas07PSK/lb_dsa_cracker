class Solution:
    def help_classmate (self, arr, n):
        stk, res = [], [None for i in range(n)]
        for i in range(n):
            while ((stk) and (arr[stk[-1]] > arr[i])): res[stk.pop()] = arr[i]
            stk.append(i)
        while (stk): res[stk.pop()] = -1
        return res
