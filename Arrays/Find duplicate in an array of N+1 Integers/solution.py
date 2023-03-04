class Solution:
    def findDuplicate (self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        slow, fast = nums[slow], nums[nums[fast]]
        while (slow != fast): slow, fast = nums[slow], nums[nums[fast]]
        fast = nums[0]
        while (slow != fast): slow, fast = nums[slow], nums[fast]
        return slow
