class Solution:
    def rotate (self, nums: List[int], k: int) -> None:
        k %= len(nums)
        for i in range(len(nums) // 2):
            nums[i], nums[len(nums) - i - 1] = nums[len(nums) - i - 1], nums[i]
        for i in range(k // 2):
            nums[i], nums[k - i - 1] = nums[k - i - 1], nums[i]
        for i in range((len(nums) - k + 1) // 2):
            nums[k + i], nums[len(nums) - i - 1] = nums[len(nums) - i - 1], nums[k + i]
