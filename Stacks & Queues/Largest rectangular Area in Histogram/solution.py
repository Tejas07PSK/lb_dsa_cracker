from collections from deque
class Solution:
    def getMaxArea (self, arr, n):
        stk, ans = deque(), arr[0]
        stk.append([arr[0], 1])
        for i in range(1, n):
            ans = max(ans, arr[i])
            if (arr[i] <= stk[-1][0]):
                prev_height, prev_left_spread = stk.pop()
                stk.append([arr[i], 1 + prev_left_spread])
                ans = max(ans, (stk[-1][0] * stk[-1][1]))
            else: stk.append([arr[i], 1])
        prev_height, prev_width = stk.pop()
        while (stk):
            stk[-1][1] += prev_width
            ans = max(ans, (stk[-1][0] * stk[-1][1]))
            prev_height, prev_width = stk.pop()
        return ans
