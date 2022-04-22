from collections import deque
class Solution:
    def canRepresentBST (self, arr, N):
        stk = deque() ; stk.append([arr[0], arr[0], arr[0], None])
        for i in range(1, len(arr)):
            if (arr[i] <= stk[-1][0]): stk.append([arr[i], arr[i], arr[i], stk[-1][0]])
            else:
                prev_ele, prev_min, prev_max, max_predecessor = stk.pop()
                while ((stk) and (max_predecessor != None) and (arr[i] > max_predecessor)):
                    if ((prev_ele > stk[-1][0]) and (stk[-1][0] > prev_min)): return 0
                    stk[-1][1], stk[-1][2] = min(stk[-1][1], prev_min), max(stk[-1][2], prev_max)
                    prev_ele, prev_min, prev_max, max_predecessor = stk.pop()
                stk.append([prev_ele, prev_min, prev_max, max_predecessor]) ; stk.append([arr[i], arr[i], arr[i], max_predecessor])
        prev_ele, prev_min, prev_max, max_predecessor = stk.pop()
        while (stk):
            if ((prev_ele > stk[-1][0]) and (stk[-1][0] > prev_min)): return 0
            stk[-1][1], stk[-1][2] = min(stk[-1][1], prev_min), max(stk[-1][2], prev_max)
            prev_ele, prev_min, prev_max, max_predecessor = stk.pop()
        return 1
