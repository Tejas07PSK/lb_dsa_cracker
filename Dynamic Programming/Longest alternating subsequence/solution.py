import
class Solution:
	def AlternatingaMaxLength (self, nums):
		prev_lt_sz, prev_gt_sz = 1, 1
		for i in range(1, len(nums)):
		    if (nums[i] > nums[i - 1]): prev_gt_sz = prev_lt_sz + 1
		    if (nums[i] < nums[i - 1]): prev_lt_sz = prev_gt_sz + 1
		return max(prev_lt_sz, prev_gt_sz)
