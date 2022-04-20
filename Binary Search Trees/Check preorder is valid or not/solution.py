from collections import deque
def isPreorderValid (arr):
    stk, res = deque(), 1 ; stk.append((arr[0], None))
    for i in range(1, len(arr)):
        if (arr[i] <= stk[-1][0]):
            if ((stk[-1][1] != None) and (stk[-1][0] > stk[-1][1]) and (arr[i] < stk[-1][1])):
                res = 0 ; break
            stk.append((arr[i], stk[-1][0]))
        else:
            prev = stk.pop()
            while ((stk) and (arr[i] > stk[-1][0])): prev = stk.pop()
            stk.append((arr[i], prev[0]))
    return res
