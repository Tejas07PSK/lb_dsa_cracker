from collections import deque
class Solution:
    def maxSlidingWindow (self, nums: List[int], k: int) -> List[int]:
        dq_max, dq_min, ans, min_per_win = deque(), deque(), [], 0
        for i in range(len(nums)):
            if ((dq_max) and (dq_max[0] < (i - k + 1))): dq_max.popleft()
            if ((dq_min) and (dq_min[0] < (i - k + 1))): dq_min.popleft()
            while ((dq_max) and (nums[dq_max[-1]] < nums[i])): dq_max.pop()
            while ((dq_min) and (nums[dq_min[-1]] > nums[i])): dq_min.pop()
            dq_max.append(i) ; dq_min.append(i)
            if (i >= (k - 1)): ans.append(nums[dq_max[0]] + nums[dq_min[0]])
        return ans
