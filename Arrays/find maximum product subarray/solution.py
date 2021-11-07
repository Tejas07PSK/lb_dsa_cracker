class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max, max_so_far, min_so_far =  nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            max_so_far, min_so_far = max(nums[i], (max_so_far * nums[i]), (min_so_far * nums[i])), min(nums[i], (max_so_far * nums[i]), (min_so_far * nums[i]))
            global_max = max(global_max, max_so_far)
        return global_max
