class Solution:
    def nextPermutation (self, nums: List[int]) -> None:
        i = len(nums) - 1
        while ((i > 0) and (nums[i] <= nums[i - 1])): i -= 1
        if (i > 0):
            pivot = i - 1
            while ((i < len(nums)) and (nums[i] > nums[pivot])): i += 1
            nums[pivot], nums[i - 1] = nums[i - 1], nums[pivot]
            i = pivot + 1
        j = len(nums) - 1
        while (i < j):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1 ; j -= 1
