from collections import deque
class Solution:
    def getMaxArea (self, arr):
        stk, ans, n = deque(), arr[0], len(arr)
        stk.append([arr[0], 1])
        for i in range(1, n):
            ans = max(ans, arr[i])
            prev_height, prev_width = None, None
            curr_height, curr_width = arr[i], 1
            while ((stk) and (curr_height <= stk[-1][0])):
                curr_width += stk[-1][1]
                ans = max(ans, (curr_height * curr_width))
                if (prev_height):
                    stk[-1][1] += prev_width ; ans = max(ans, (stk[-1][0] * stk[-1][1]))
                prev_height, prev_width = stk.pop()
            stk.append([curr_height, curr_width])
        prev_height, prev_width = stk.pop()
        while (stk):
            stk[-1][1] += prev_width
            ans = max(ans, (stk[-1][0] * stk[-1][1]))
            prev_height, prev_width = stk.pop()
        return ans
