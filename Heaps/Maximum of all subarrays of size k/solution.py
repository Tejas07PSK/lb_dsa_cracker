from collections import deque

class Solution:
    def max_of_subarrays (self, arr, n, k):
        dq, ans = deque(), []
        for i in range(n):
            if ((dq) and (dq[0] < (i - k + 1))): dq.popleft()
            while ((dq) and (arr[dq[-1]] < arr[i])): dq.pop()
            dq.append(i)
            if (i >= (k - 1)): ans.append(arr[dq[0]])
        return ans
