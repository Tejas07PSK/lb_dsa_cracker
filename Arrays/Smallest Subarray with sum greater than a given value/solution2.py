class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j, sum, n = 0, 0, 0, len(nums)
        res = (n + 1)
        while (j < n):
            sum += nums[j]
            while (sum >= target):
                res = min(res, (j - i + 1))
                sum -= nums[i]
                i += 1
            j += 1
        return (0 if res == (n + 1) else res)
