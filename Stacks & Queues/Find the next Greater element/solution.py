from collections import deque
class Solution:
    def nextLargerElement (self, arr, n):
        stk, res = deque(), [-1 for i in range(n)]
        for i in range(n):
            while ((stk) and (arr[i] > arr[stk[-1]])): res[stk.pop()] = arr[i]
            stk.append(i)
        return res
